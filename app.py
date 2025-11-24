import streamlit as st
import os
from dotenv import load_dotenv
from services.email_processor import EmailProcessor
from services.prompt_manager import PromptManager
from services.draft_manager import DraftManager
from services.llm_service import LLMService
from utils.helpers import format_timestamp

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="Email Productivity Agent",
    page_icon="📧",
    layout="wide"
)

# Initialize Services
def get_services():
    return {
        "email_processor": EmailProcessor(),
        "prompt_manager": PromptManager(),
        "draft_manager": DraftManager(),
        "llm_service": LLMService()
    }

services = get_services()

# Sidebar Navigation
st.sidebar.title("📧 Email Agent")
page = st.sidebar.radio(
    "Navigate",
    ["Inbox", "Prompt Brain", "Email Agent", "Drafts"]
)

# API Key Check
if not os.getenv("GEMINI_API_KEY"):
    st.error("⚠️ GEMINI_API_KEY not found in environment variables. Please configure it in .env file.")
    st.stop()

def render_inbox():
    st.title("📥 Inbox")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Manage and process your emails.")
    with col2:
        if st.button("⚡ Process Inbox", type="primary"):
            with st.spinner("Processing emails..."):
                count = services["email_processor"].process_inbox()
                st.success(f"Processed {count} emails!")
                st.rerun()

    # Filter
    filter_category = st.selectbox(
        "Filter by Category",
        ["All", "Important", "To-Do", "Newsletter", "Spam", "Project", "Personal", "Uncategorized"]
    )

    emails = services["email_processor"].emails
    
    # Apply Filter
    if filter_category != "All":
        if filter_category == "Uncategorized":
            emails = [e for e in emails if not e.category]
        else:
            emails = [e for e in emails if e.category == filter_category]

    # Display Emails
    for email in emails:
        with st.expander(f"{'🔴 ' if not email.processed else ''}{email.sender} - {email.subject}"):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"**Date:** {format_timestamp(email.timestamp)}")
                st.markdown(f"**Category:** {email.category or 'Uncategorized'}")
                st.markdown("---")
                st.write(email.body)
                
                if email.action_items:
                    st.markdown("### 📋 Action Items")
                    for item in email.action_items:
                        st.info(f"**Task:** {item.get('task')}\n\n**Deadline:** {item.get('deadline') or 'None'}")
            
            with c2:
                if st.button("Summarize", key=f"sum_{email.id}"):
                    prompt = services["prompt_manager"].get_prompt("summarization")
                    if prompt:
                        with st.spinner("Summarizing..."):
                            summary = services["llm_service"].generate_response(
                                prompt.template, 
                                f"Email Body:\n{email.body}"
                            )
                            st.write(summary)
                
                if st.button("Draft Reply", key=f"reply_{email.id}"):
                    # Set session state to navigate to drafts or open modal
                    st.session_state['reply_email'] = email
                    st.toast("Go to 'Drafts' or 'Email Agent' to finalize.")


def render_prompt_brain():
    st.title("🧠 Prompt Brain")
    st.write("Customize the agent's behavior by editing prompts.")
    
    prompts = services["prompt_manager"].get_all_prompts()
    
    if not prompts:
        st.error("⚠️ No prompts found. Please check that data/prompts.json exists.")
        return
    
    tabs = st.tabs([p.name for p in prompts.values()])
    
    for i, (key, prompt) in enumerate(prompts.items()):
        with tabs[i]:
            st.markdown(f"**Description:** {prompt.description}")
            new_template = st.text_area(
                "Template",
                value=prompt.template,
                height=300,
                key=f"prompt_{key}"
            )
            
            if st.button("Save Changes", key=f"save_{key}"):
                services["prompt_manager"].update_prompt(key, new_template)
                st.success("Prompt updated successfully!")

def render_email_agent():
    st.title("🤖 Email Agent")
    st.write("Chat with your inbox.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about your emails..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Build context from inbox
                emails = services["email_processor"].emails
                
                # Create a summary of the inbox for context
                inbox_summary = "Here is the current inbox:\n\n"
                for email in emails:
                    inbox_summary += f"- From: {email.sender}\n"
                    inbox_summary += f"  Subject: {email.subject}\n"
                    inbox_summary += f"  Category: {email.category or 'Uncategorized'}\n"
                    if email.action_items:
                        inbox_summary += f"  Action Items: {len(email.action_items)} tasks\n"
                    inbox_summary += f"  Preview: {email.body[:100]}...\n\n"
                
                # Construct the prompt
                system_prompt = f"""You are a helpful email assistant. Answer the user's question based on their inbox.
                
{inbox_summary}

User Question: {prompt}

Provide a helpful, concise answer based on the inbox data above."""
                
                response = services["llm_service"].generate_response(system_prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

def render_drafts():
    st.title("📝 Drafts")
    
    # Section 1: Generate new draft
    with st.expander("➕ Generate New Draft", expanded='reply_email' in st.session_state):
        if 'reply_email' in st.session_state:
            email = st.session_state['reply_email']
            st.info(f"Drafting reply to: **{email.subject}** from **{email.sender}**")
            
            col1, col2 = st.columns(2)
            with col1:
                instructions = st.text_area("Instructions for reply", "Polite and professional.", key="reply_instructions")
            with col2:
                tone = st.selectbox("Tone", ["Professional", "Casual", "Urgent"], key="reply_tone")
                
            if st.button("Generate Draft", type="primary"):
                prompt = services["prompt_manager"].get_prompt("auto_reply")
                if prompt:
                    with st.spinner("Generating..."):
                        # Construct context
                        context_vars = {
                            "user_instructions": f"{instructions}. Tone: {tone}",
                            "sender": email.sender,
                            "subject": email.subject,
                            "body": email.body
                        }
                        filled_template = prompt.template.format(**context_vars)
                        
                        draft_body = services["llm_service"].generate_response(filled_template)
                        
                        services["draft_manager"].create_draft(
                            subject=f"Re: {email.subject}",
                            body=draft_body,
                            email_id=email.id
                        )
                        del st.session_state['reply_email']
                        st.success("✅ Draft created!")
                        st.rerun()
        else:
            st.write("Select an email from the Inbox and click 'Draft Reply', or create a new draft below:")
            
            # Allow creating a draft from scratch
            new_subject = st.text_input("Subject", placeholder="Enter email subject")
            new_instructions = st.text_area("What should this email say?", placeholder="E.g., Thank them for the meeting and confirm next steps")
            
            if st.button("Generate New Draft", type="primary"):
                if new_subject and new_instructions:
                    with st.spinner("Generating..."):
                        prompt_text = f"Write a professional email with the following subject and content:\n\nSubject: {new_subject}\n\nContent: {new_instructions}\n\nWrite only the email body, no subject line."
                        draft_body = services["llm_service"].generate_response(prompt_text)
                        
                        services["draft_manager"].create_draft(
                            subject=new_subject,
                            body=draft_body
                        )
                        st.success("✅ Draft created!")
                        st.rerun()
                else:
                    st.warning("Please fill in both subject and instructions.")

    st.markdown("---")
    st.markdown("### 📋 Saved Drafts")
    
    drafts = services["draft_manager"].get_all_drafts()
    
    if not drafts:
        st.info("No drafts yet. Generate one above!")
    
    for draft in drafts:
        with st.expander(f"✉️ {draft.subject} - {format_timestamp(draft.created_at)}"):
            new_subject = st.text_input("Subject", value=draft.subject, key=f"subj_{draft.id}")
            new_body = st.text_area("Body", value=draft.body, height=200, key=f"body_{draft.id}")
            
            c1, c2, c3 = st.columns([1, 1, 1])
            with c1:
                if st.button("💾 Save", key=f"save_draft_{draft.id}"):
                    services["draft_manager"].update_draft(draft.id, new_subject, new_body)
                    st.success("Saved!")
            with c2:
                if st.button("📋 Copy", key=f"copy_draft_{draft.id}"):
                    st.code(new_body, language=None)
                    st.info("Copy the text above!")
            with c3:
                if st.button("🗑️ Delete", key=f"del_draft_{draft.id}", type="secondary"):
                    services["draft_manager"].delete_draft(draft.id)
                    st.rerun()

# Routing
if page == "Inbox":
    render_inbox()
elif page == "Prompt Brain":
    render_prompt_brain()
elif page == "Email Agent":
    render_email_agent()
elif page == "Drafts":
    render_drafts()
