from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    
    message_id : int = None
    message : str
    user_id : int=None

    def set_user_id(self,user_id):
        self.user_id= user_id
    def set_msg_id(self,message_id):
        self.message_id=message_id;