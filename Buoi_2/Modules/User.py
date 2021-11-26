from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    
    user_id: int = None
    full_name: Optional[str]=None
    username:  str
    password:   str

    def set_user_id(self,user_id):
        self.user_id=user_id

        
    
    