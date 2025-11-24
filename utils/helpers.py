import uuid
import re
from datetime import datetime

def generate_id():
    """Generate a unique ID."""
    return str(uuid.uuid4())

def format_timestamp(timestamp_str):
    """Format ISO timestamp to human readable string."""
    try:
        dt = datetime.fromisoformat(timestamp_str)
        return dt.strftime("%b %d, %Y %I:%M %p")
    except ValueError:
        return timestamp_str

def sanitize_input(text):
    """Basic input sanitization."""
    if not text:
        return ""
    return text.strip()

def extract_json_from_text(text):
    """Extract JSON object from text that might contain markdown code blocks."""
    try:
        # Try to find JSON inside code blocks
        match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
        if match:
            return match.group(1)
        # Or just look for the first { and last }
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return match.group(0)
        return text
    except Exception:
        return text
