
import json
from Modules.message import Message
from fastapi.encoders import jsonable_encoder

class message_service:
    def read_message():
        with open("message.json","r") as file:
            list_message = json.load(file)
        return list_message;

    def save_message(message: Message):
        # doc du lieu tu file message
        list_message = message_service.read_message()

        message.set_msg_id(len(list_message) +1)
        # convert message -> json
        data = jsonable_encoder(message)

        list_message.append(data)
        with open("message.json","w") as file:
            json.dump(list_message, file)
        return {"message":"success"}
    
    def get_message(user_id: int):
        list_message = message_service.read_message()
        list_msg_response=[]

        for msg in list_message:
            if msg.get("user_id") == user_id: 
                data = {"message_id": msg.get("message_id"), "message": msg.get("message") }
                list_msg_response.append(data);
    
        return list_msg_response

    
    