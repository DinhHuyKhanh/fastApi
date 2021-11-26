from fastapi import FastAPI,Depends
from fastapi.encoders import jsonable_encoder
from Modules.message_service import message_service
from Modules.user import User
from Modules.authenticator import Authenticator,Verify_token
from Modules.message import Message
from Modules.user_service import user_service;


app = FastAPI()
    
@app.post("/user")
async def register_user(user: User):
    return user_service.save_user(user=user)


@app.post("/login")
async def login(login : User):

    return Authenticator.login(login=login)


@app.post("/message")
async def create_message(message: Message, authorized = Depends(Verify_token.verify_token)):
        message.set_user_id (authorized)

        return message_service.save_message(message=message)


@app.get("/message")
async def get_message(authorized = Depends(Verify_token.verify_token)):
    
    return message_service.get_message(authorized)




