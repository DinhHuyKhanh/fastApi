
from Entity import User

import secrets
class Authenticator:
    token_map={}

    def create_token(user: User):
        token = secrets.token_urlsafe(256)
        Authenticator.set_token_user(token=token,user=user)
        return {token}

    def set_token_user(self,token: str,user: User):
        self.token_map["Bearer "+token]=user;

    def get_token_user(self,token: str):
        if self.token_map.get(token) != None :
            return self.token_map.get(token)
        return False