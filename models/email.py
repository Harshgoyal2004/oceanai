from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str
    timestamp: str
    category: Optional[str] = None
    action_items: Optional[List[Dict[str, Any]]] = None
    processed: bool = False

    def to_dict(self):
        return self.model_dump()
