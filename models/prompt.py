from pydantic import BaseModel

class Prompt(BaseModel):
    name: str
    description: str
    template: str

    def to_dict(self):
        return self.model_dump()
