from fastapi import FastAPI,Request,Depends
from fastapi.encoders import jsonable_encoder
from utils import utils
from Modules.User import User
from Modules.Authenticator import Authenticator
from Modules.Message import Message

app = FastAPI()

def verify_token(request: Request):
    token = request.headers.get('Authorization')
    if token:
        data= Authenticator.get_token_user(token=token)
        if data == False:
            return False
        return data
    return False;

    
@app.post("/user")
async def register_user(user: User):
    list_users = utils.read_users()

    user.set_user_id(len(list_users) + 1)
    data = jsonable_encoder(user)

    for u in list_users :
        if u.get("username") == user.username : 
            return {"message":"User already exists"}

    list_users.append(data)
    utils.save_user(list_users=list_users)

    return {"message":"success"}


@app.post("/login")
async def login(login : User):
    list_user = utils.read_users()
    for u in list_user :
       if u["username"] == login.username and u["password"]== login.password:
           return {"full_name": u["full_name"],"token": Authenticator.create_token(user=u)}
    return {"message":"login fail"}


@app.post("/message")
async def create_message(message: Message, authorized = Depends(verify_token)):
    if authorized:
        # doc du lieu tu file message
        list_message = utils.read_message()
        
        message.set_user_id (authorized.get("user_id"))
        message.set_msg_id(len(list_message) +1)
        # convert message -> json
        data = jsonable_encoder(message)

        list_message.append(data)
        utils.save_message(list_message=list_message)

        return {"message":"success"}
    return {"message":"fail"}


@app.get("/message")
async def get_message(authorized = Depends(verify_token)):
    if authorized : 
        list_message = utils.read_message()
        list_msg_response=[]

        for msg in list_message:
            if(msg.get("user_id") == authorized.get("user_id") ): 
                data = {"message_id": msg.get("message_id"), "message": msg.get("message") }
                list_msg_response.append(data);
    
        return list_msg_response

    return {"message":"fail"}




