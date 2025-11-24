import json
import os
from models.prompt import Prompt

class PromptManager:
    def __init__(self, prompts_file="data/prompts.json"):
        # Use path relative to this file's directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.prompts_file = os.path.join(base_dir, prompts_file)
        self.prompts = self.load_prompts()

    def load_prompts(self):
        """Load prompts from JSON file."""
        if not os.path.exists(self.prompts_file):
            return {}
        
        try:
            with open(self.prompts_file, 'r') as f:
                data = json.load(f)
                prompts = {}
                for key, value in data.items():
                    prompts[key] = Prompt(**value)
                return prompts
        except Exception as e:
            print(f"Error loading prompts: {e}")
            return {}

    def save_prompts(self):
        """Save prompts to JSON file."""
        try:
            data = {k: v.to_dict() for k, v in self.prompts.items()}
            with open(self.prompts_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving prompts: {e}")
            return False

    def get_prompt(self, key):
        """Get a specific prompt by key."""
        return self.prompts.get(key)

    def update_prompt(self, key, template):
        """Update a prompt template."""
        if key in self.prompts:
            self.prompts[key].template = template
            return self.save_prompts()
        return False

    def get_all_prompts(self):
        """Return all prompts."""
        return self.prompts
