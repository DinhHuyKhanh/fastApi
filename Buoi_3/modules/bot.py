

from typing import Optional
from pydantic import BaseModel

class Bot(BaseModel):
    name: str
    description: Optional[str]=None
    enabled: bool
    config: Optional[str]=None
    owner: Optional[int] = None  

