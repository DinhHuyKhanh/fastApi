from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int = None
    full_name: Optional[str]=None
    username:  str
    password:   str
    def set_user_id(self,user_id):
        self.user_id=user_id

class LoginRequest(BaseModel):
    username: Optional[str]=None
    password: Optional[str]=None
class Message(BaseModel):
    message_id : int = None
    message : str
    user_id : int=None
 
    def set_user_id(self,user_id):
        self.user_id= user_id
    def set_msg_id(self,message_id):
        self.message_id=message_id;

