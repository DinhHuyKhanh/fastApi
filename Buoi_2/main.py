
from os import P_NOWAIT
from fastapi import FastAPI,Request,Depends
from fastapi.encoders import jsonable_encoder
from Entity import User,LoginRequest, Message
from utils import utils
from Authenticator import Authenticator


app = FastAPI()

def verify_token(request: Request):
    token = request.headers.get('Authorization')
    if token:
        data= Authenticator.get_token_user(Authenticator ,token=token)
        if(data == None):
            return False
        return data
    return False;

    
@app.post("/user")
async def register_user(user: User):
    list_users = utils.read_users()

    user.set_user_id(len(list_users) + 1)
    data = jsonable_encoder(user)

    for u in list_users :
        if(u.get("username") == user.get_username() ): 
            return {"User already exists"}

    list_users.append(data)
    utils.save_user(list_users=list_users)

    return {"success"}


@app.post("/login")
async def login(login : LoginRequest):
    list_user = utils.read_users()
    for u in list_user :
       if u["username"] == login.get_username() and u["password"]== login.get_password():
           return {"full_name": u["full_name"],"token": Authenticator.create_token(user=u)}
    return {"login fail"}


@app.post("/message")
async def create_message(message: Message, authorized: str =Depends(verify_token)):
    if(authorized):
        # doc du lieu tu file message
        list_message = utils.read_message()
        
        message.set_user_id (authorized.get("user_id"))
        message.set_msg_id(len(list_message) +1)
        # convert message -> json
        data = jsonable_encoder(message)

        list_message.append(data)
        utils.save_message(list_message=list_message)

        return {"success"}
    return "fail"


@app.get("/message")
async def get_message(authorized: str= Depends(verify_token)):
    if (authorized): 
        list_message = utils.read_message()
        list_msg_response=[]

        for msg in list_message:
            if(msg.get("user_id") == authorized.get("user_id") ): 
                data = {"message_id": msg.get("message_id"), "message": msg.get("message") }
                list_msg_response.append(data);
    
        return list_msg_response

    return {"fail"}




