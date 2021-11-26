import secrets
from Modules.message import Message
from Modules.user import User
from fastapi import Request
from Modules.user_service import user_service

class Authenticator:

    token_map={}

    def create_token(user: User):
        token = secrets.token_urlsafe(256)
        Authenticator.token_map["Bearer " +token] = user
        return token

    def login(login:User):
        list_users= user_service.read_users();
        for u in list_users :
            if u["username"] == login.username and u["password"]== login.password:
             return {"full_name": u["full_name"],"token": Authenticator.create_token(user=u)}
        return {"message":"login fail"}

class Verify_token:
    def verify_token(request: Request):
        token = request.headers.get('Authorization')
        if token:
             data= Authenticator.token_map.get(token)
             if data :
                return data.get("user_id")
        raise Exception("No data")
