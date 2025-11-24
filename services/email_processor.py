import json
import os
from models.email import Email
from services.llm_service import LLMService
from services.prompt_manager import PromptManager

class EmailProcessor:
    def __init__(self, inbox_file="data/mock_inbox.json"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.inbox_file = os.path.join(base_dir, inbox_file)
        self.llm_service = LLMService()
        self.prompt_manager = PromptManager()
        self.emails = self.load_emails()

    def load_emails(self):
        """Load emails from JSON file."""
        if not os.path.exists(self.inbox_file):
            return []
        
        try:
            with open(self.inbox_file, 'r') as f:
                data = json.load(f)
                return [Email(**e) for e in data]
        except Exception as e:
            print(f"Error loading emails: {e}")
            return []

    def save_emails(self):
        """Save emails to JSON file."""
        try:
            data = [e.to_dict() for e in self.emails]
            with open(self.inbox_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving emails: {e}")
            return False

    def get_email(self, email_id):
        """Get a specific email by ID."""
        for email in self.emails:
            if email.id == email_id:
                return email
        return None

    def process_email(self, email_id):
        """Process a single email: Categorize and Extract Action Items."""
        email = self.get_email(email_id)
        if not email:
            return False

        # 1. Categorize
        cat_prompt = self.prompt_manager.get_prompt("categorization")
        if cat_prompt:
            category = self.llm_service.generate_response(
                cat_prompt.template, 
                f"Email Body:\n{email.body}"
            )
            email.category = category.strip()

        # 2. Extract Action Items
        action_prompt = self.prompt_manager.get_prompt("action_extraction")
        if action_prompt:
            context = action_prompt.template.replace("{email_body}", email.body)
            result = self.llm_service.generate_json(context)
            if result and 'tasks' in result:
                email.action_items = result['tasks']

        email.processed = True
        self.save_emails()
        return True

    def process_inbox(self):
        """Process all unprocessed emails."""
        count = 0
        for email in self.emails:
            if not email.processed:
                self.process_email(email.id)
                count += 1
        return count

    def search_emails(self, query):
        """Simple search implementation."""
        query = query.lower()
        results = []
        for email in self.emails:
            if (query in email.subject.lower() or 
                query in email.sender.lower() or 
                query in email.body.lower()):
                results.append(email)
        return results
