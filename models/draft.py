from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class Draft(BaseModel):
    id: str
    email_id: Optional[str] = None
    subject: str
    body: str
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    metadata: Optional[Dict[str, Any]] = {}

    def to_dict(self):
        return self.model_dump()
