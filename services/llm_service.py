import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from utils.helpers import extract_json_from_text

# Load environment variables
load_dotenv()

class LLMService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            # For development/testing without key, we might want to warn or handle gracefully
            print("Warning: GEMINI_API_KEY not found in environment variables.")
            self.model = None
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate_response(self, prompt_text, context=""):
        """
        Generate a response from the LLM.
        """
        if not self.model:
            return "Error: LLM not configured. Please check your API key."

        try:
            full_prompt = f"{prompt_text}\n\n{context}"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def generate_json(self, prompt_text, context=""):
        """
        Generate a JSON response from the LLM.
        """
        if not self.model:
            return {}

        try:
            full_prompt = f"{prompt_text}\n\n{context}\n\nIMPORTANT: Respond with valid JSON only."
            response = self.model.generate_content(full_prompt)
            json_str = extract_json_from_text(response.text)
            return json.loads(json_str)
        except json.JSONDecodeError:
            print(f"Failed to decode JSON from LLM response: {response.text}")
            return {}
        except Exception as e:
            print(f"Error generating JSON: {str(e)}")
            return {}
