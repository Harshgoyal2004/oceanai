import os
import sys
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.email_processor import EmailProcessor
from services.prompt_manager import PromptManager
from services.draft_manager import DraftManager
from services.llm_service import LLMService

def test_services():
    print("Testing Services...")
    
    # 1. Test Prompt Manager
    pm = PromptManager()
    prompts = pm.get_all_prompts()
    print(f"Loaded {len(prompts)} prompts.")
    assert "categorization" in prompts
    assert "action_extraction" in prompts
    print("✅ PromptManager working.")

    # 2. Test Email Processor
    ep = EmailProcessor()
    emails = ep.emails
    print(f"Loaded {len(emails)} emails.")
    assert len(emails) > 0
    print("✅ EmailProcessor loading working.")

    # 3. Test Draft Manager
    dm = DraftManager()
    drafts = dm.get_all_drafts()
    print(f"Loaded {len(drafts)} drafts.")
    
    # Create a dummy draft
    draft = dm.create_draft("Test Subject", "Test Body")
    assert len(dm.get_all_drafts()) == len(drafts) + 1
    dm.delete_draft(draft.id)
    assert len(dm.get_all_drafts()) == len(drafts)
    print("✅ DraftManager CRUD working.")

    print("\nAll backend services verified successfully!")

if __name__ == "__main__":
    test_services()
