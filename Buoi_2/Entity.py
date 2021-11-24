from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    user_id: int = None
    full_name: Optional[str]=None
    username:  str
    password:   str

    def get_user_id(self):
        return self.user_id
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def set_user_id(self,user_id):
        self.user_id=user_id

class LoginRequest(BaseModel):
    username: Optional[str]=None
    password: Optional[str]=None
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    
class Message(BaseModel):
    message_id : int = None
    message : str
    user_id : int=None
    def get_message_id(self):
        return self.message_id
    def get_message(self):
        return self.message
    def set_user_id(self,user_id):
        self.user_id= user_id
    def set_msg_id(self,message_id):
        self.message_id=message_id;

