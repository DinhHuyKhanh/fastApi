from typing import Optional
from pydantic import BaseModel


class Entity(BaseModel):
    name: str
    bg_color: Optional[str]=None
    fg_color: Optional[str]=None,
    bot: str

    
