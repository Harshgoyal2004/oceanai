import json
import os
from models.draft import Draft
from utils.helpers import generate_id

class DraftManager:
    def __init__(self, drafts_file="data/drafts.json"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.drafts_file = os.path.join(base_dir, drafts_file)
        self.drafts = self.load_drafts()

    def load_drafts(self):
        """Load drafts from JSON file."""
        if not os.path.exists(self.drafts_file):
            return []
        
        try:
            with open(self.drafts_file, 'r') as f:
                data = json.load(f)
                return [Draft(**d) for d in data]
        except Exception as e:
            print(f"Error loading drafts: {e}")
            return []

    def save_drafts(self):
        """Save drafts to JSON file."""
        try:
            data = [d.to_dict() for d in self.drafts]
            with open(self.drafts_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving drafts: {e}")
            return False

    def create_draft(self, subject, body, email_id=None, metadata=None):
        """Create a new draft."""
        draft = Draft(
            id=generate_id(),
            email_id=email_id,
            subject=subject,
            body=body,
            metadata=metadata or {}
        )
        self.drafts.append(draft)
        self.save_drafts()
        return draft

    def update_draft(self, draft_id, subject, body):
        """Update an existing draft."""
        for draft in self.drafts:
            if draft.id == draft_id:
                draft.subject = subject
                draft.body = body
                return self.save_drafts()
        return False

    def delete_draft(self, draft_id):
        """Delete a draft."""
        self.drafts = [d for d in self.drafts if d.id != draft_id]
        return self.save_drafts()

    def get_draft(self, draft_id):
        """Get a specific draft."""
        for draft in self.drafts:
            if draft.id == draft_id:
                return draft
        return None

    def get_all_drafts(self):
        """Get all drafts."""
        return self.drafts
