import secrets
from Modules.User import User

class Authenticator:

    token_map={}

    def create_token(user: User):
        token = secrets.token_urlsafe(256)
        Authenticator.set_token_user(token=token,user=user)
        return {token}

    def set_token_user(token: str,user: User):
        Authenticator.token_map["Bearer "+token]=user;

    def get_token_user(token: str):
        if Authenticator.token_map.get(token) != None :
            return Authenticator.token_map.get(token)
        return False