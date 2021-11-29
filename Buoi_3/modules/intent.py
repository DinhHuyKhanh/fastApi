
from pydantic import BaseModel

class Intent(BaseModel):
    name: str
    description: str
    bot: str