# 🎬 Video Demo Recording Script

**Duration**: 15 minutes maximum  
**Format**: Screen recording with voiceover  
**Upload**: Google Drive

---

## 🎯 Recording Checklist

### Before Recording
- [ ] Close unnecessary applications
- [ ] Clear browser tabs
- [ ] Test microphone audio
- [ ] Prepare `.env` file with API key
- [ ] Have application ready to run
- [ ] Review this script
- [ ] Set screen resolution to 1080p
- [ ] Turn off notifications

---

## 📝 Script Timeline

### **[0:00 - 1:00] Introduction**

> "Hello! My name is [Your Name], and today I'll be presenting my Email Productivity Agent - an intelligent, prompt-driven system that automates email management tasks using Large Language Models.
>
> This project demonstrates how AI can help users categorize emails, extract action items, and draft responses automatically. The entire system is driven by customizable prompts, making it flexible and adaptable to different use cases.
>
> Let me walk you through the code architecture, demonstrate the features, and explain my development approach."

**Show**: Project folder structure in VS Code

---

### **[1:00 - 3:00] Project Structure & Architecture**

> "First, let me show you how the project is organized."

**Show**: File explorer with folder structure

> "The application follows a clean, modular architecture:
>
> - `app.py` is the main Streamlit application that handles the UI
> - The `models` folder contains data classes for Emails, Prompts, and Drafts
> - The `services` folder has the core business logic:
>   - `llm_service.py` handles all interactions with Google's Gemini API
>   - `email_processor.py` processes emails using LLM
>   - `prompt_manager.py` manages the prompt system
> - The `data` folder stores our mock inbox, prompts, and generated drafts
> - The `utils` folder has helper functions"

**Show**: Click through each folder briefly

---

### **[3:00 - 5:00] Core Components Deep Dive**

#### Prompt-Driven Architecture (1 min)

**Open**: `data/prompts.json`

> "The key innovation here is the prompt-driven architecture. All AI behavior is controlled through these prompts stored in JSON format.
>
> We have prompts for:
> - Email categorization
> - Action item extraction
> - Reply drafting
> - General inbox chat
>
> Users can edit these prompts through the UI, making the agent highly customizable without changing code."

#### LLM Integration (1 min)

**Open**: `services/llm_service.py`

> "Here's the LLM service that interfaces with Google's Gemini API. It handles:
> - API authentication using environment variables
> - Prompt formatting
> - Response generation
> - Error handling
>
> The service is designed to be reusable across different features."

**Highlight**: Key functions like `generate_response()`

---

### **[5:00 - 6:00] Email Processing Logic**

**Open**: `services/email_processor.py`

> "The email processor is where the magic happens. It:
> 1. Loads prompts from the prompt manager
> 2. Formats emails with the appropriate prompt
> 3. Calls the LLM service
> 4. Parses and structures the response
>
> This modular design makes it easy to add new processing features."

**Highlight**: `categorize_emails()` and `extract_action_items()` functions

---

### **[6:00 - 11:00] Live Demonstration**

#### Setup & Launch (1 min)

**Show**: Terminal

> "Let me show you how to run the application. First, we need to install dependencies and set up the API key."

```bash
# Show .env file (blur the actual API key)
cat .env

# Run the application
streamlit run app.py
```

**Show**: Application launching in browser

---

#### Feature Walkthrough (4 min)

**1. Inbox View (45 sec)**

> "This is the main inbox view. It loads emails from our mock inbox JSON file. Each email shows the sender, subject, and preview."

**Show**: Scroll through inbox

**Click**: "Process Inbox" button

> "When I click Process Inbox, the LLM categorizes each email and extracts action items."

**Show**: Wait for processing, show results

---

**2. Prompt Brain (1 min)**

**Navigate**: Prompt Brain page

> "This is the Prompt Brain - the control center for the agent's behavior. Here I can view and edit all the prompts that drive the AI.
>
> Let me edit the categorization prompt to show how flexible this is."

**Action**:
- Select "Email Categorization" prompt
- Click "Edit Prompt"
- Make a small change (e.g., add a new category)
- Click "Save Changes"

> "The changes are saved immediately and will affect all future categorizations."

---

**3. Email Agent Chat (1.5 min)**

**Navigate**: Email Agent page

> "The Email Agent provides a chat interface to interact with your inbox using natural language."

**Demo queries**:
1. Type: "Summarize the email from John"
   - **Show**: Response
   
2. Type: "What are my urgent tasks?"
   - **Show**: Response
   
3. Type: "Draft a reply to the meeting request"
   - **Show**: Generated draft

> "The agent understands context and can perform various tasks based on your questions."

---

**4. Drafts Management (45 sec)**

**Navigate**: Drafts page

> "All generated email drafts are saved here. Users can review, edit, and manage them before sending."

**Show**: List of drafts, click to view one

---

### **[11:00 - 13:00] Development Approach & Workflow**

> "Let me explain my development approach for this project.
>
> **Architecture Design**: I started by designing a prompt-driven architecture because it provides maximum flexibility. Users can customize AI behavior without touching code.
>
> **Technology Stack**: I chose:
> - Streamlit for rapid UI development
> - Google Gemini for state-of-the-art LLM capabilities
> - JSON for simple data persistence
> - Python for clean, maintainable code
>
> **Development Process**:
> 1. First, I built the data models to structure emails, prompts, and drafts
> 2. Then created the LLM service as the foundation
> 3. Implemented email processing logic
> 4. Built the Streamlit UI with multiple pages
> 5. Added prompt management capabilities
> 6. Tested with various email scenarios
>
> **Challenges & Solutions**:
> - **Challenge**: Managing LLM response consistency
>   - **Solution**: Structured prompts with clear output format instructions
> 
> - **Challenge**: State management in Streamlit
>   - **Solution**: Used session state effectively for data persistence
>
> - **Challenge**: Making the system truly prompt-driven
>   - **Solution**: Centralized prompt management with JSON storage
>
> **Testing Methodology**:
> - Created diverse mock emails to test categorization
> - Tested edge cases (empty emails, long emails)
> - Verified prompt editing doesn't break functionality
> - Ensured error handling for API failures"

---

### **[13:00 - 14:30] Code Quality & Best Practices**

**Show**: Code in VS Code

> "I followed Python best practices throughout:
>
> - **Modular Design**: Separated concerns into models, services, and utils
> - **Type Hints**: Used type annotations for better code clarity
> - **Error Handling**: Implemented try-catch blocks for API calls
> - **Environment Variables**: Kept API keys secure using .env files
> - **Documentation**: Added docstrings to key functions
> - **Clean Code**: Followed PEP 8 style guidelines
> - **Version Control**: Used Git with meaningful commit messages"

**Show**: Example of well-documented function

---

### **[14:30 - 15:00] Conclusion & Future Enhancements**

> "To summarize, I've built a fully functional Email Productivity Agent that:
> - Automatically categorizes emails
> - Extracts action items
> - Drafts replies using AI
> - Provides a chat interface for inbox interaction
> - Allows complete customization through prompt editing
>
> **Future Enhancements** could include:
> - Integration with real email providers (Gmail, Outlook)
> - Multi-language support
> - Email scheduling
> - Advanced analytics and insights
> - Calendar integration for action items
>
> **Deployment**: The application is deployed at [mention your URL] and the code is available on GitHub.
>
> Thank you for watching! I hope this demonstration clearly shows the capabilities and architecture of the Email Productivity Agent."

**Show**: Final view of running application

---

## 🎥 Recording Tips

### Camera & Audio
- Use a good microphone (or at least test built-in mic)
- Speak clearly and at moderate pace
- Pause briefly between sections
- Smile (it comes through in your voice!)

### Screen Recording
- Use 1920x1080 resolution
- Record at 30fps minimum
- Use cursor highlighting if available
- Zoom in on code when explaining details

### Editing (Optional)
- Cut out long pauses
- Add transitions between sections
- Include text overlays for key points
- Add background music (low volume)

### Tools
- **macOS**: QuickTime Player, ScreenFlow
- **Windows**: OBS Studio, Camtasia
- **Cross-platform**: Loom, Zoom

---

## ✅ Pre-Recording Checklist

- [ ] Script reviewed and practiced
- [ ] Application tested and working
- [ ] Mock data prepared
- [ ] Screen resolution set to 1080p
- [ ] Microphone tested
- [ ] Notifications disabled
- [ ] Browser tabs cleaned up
- [ ] Recording software ready
- [ ] Timer/clock visible (to track 15 min)

---

## 📤 Post-Recording

1. **Review the video**
   - Watch completely
   - Check audio quality
   - Verify all features shown
   - Confirm duration ≤ 15 minutes

2. **Export settings**
   - Format: MP4
   - Resolution: 1080p
   - Codec: H.264
   - Audio: AAC

3. **Upload to Google Drive**
   - Set sharing to "Anyone with link"
   - Copy shareable link
   - Add to README.md

4. **Update repository**
   ```bash
   git add README.md
   git commit -m "Add video demo link"
   git push origin main
   ```

---

## 🎬 Action!

You're ready to record! Remember:
- Be enthusiastic but natural
- Take your time explaining concepts
- Show, don't just tell
- Stay within 15 minutes
- Have fun with it!

Good luck! 🌟
