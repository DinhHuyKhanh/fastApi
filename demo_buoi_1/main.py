from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()

class Message(BaseModel):
    message_id: int
    message : str
    def get_message_id(self):
        return self.message_id
    def get_message(self):
        return self.message


def read_data():
    with open("data.json","r") as file:
        list_message = json.load(file)
    return list_message;



## get ALL message
@app.get("/bot/message/")
async def get_message():
    list_message = read_data();
    return list_message;


## method: get message by id
@app.get("/bot/message/id/{id}")
async def get_message_by_id(id: int):
    list_message= read_data()

    if(id>len(list_message) or id<=0):
        return {"message":"không tồn tại!"}

    return list_message[id-1]


# method: create message
@app.post("/bot/message/create")
async def create_message(message: Message):

    # tạo json từ class Message
    data={"message_id":  message.message_id, "message": message.message}
    
    #đọc dữ liệu từ file
    list_message = read_data()
    for mess in list_message:
        if(mess["message_id"] == message.get_message_id() ):
            return {"message: đã tồn tại message có id": message.get_message_id()}
    list_message.append(data)

    # luu file 
    with open("data.json","w") as file:
        json.dump(list_message, file)

    return {"status": "success"}


# method delete by id
@app.delete("/bot/message/delete/id/{id}")
async def delete_message_by_id(id: int):
    list_message = read_data()
    index = 0 
    
    for mess in list_message:
        if(mess["message_id"] == id):
            list_message.pop(index)
        index+=1
    
     # luu file 
    with open("data.json","w") as file:
        json.dump(list_message, file)

    return {"message:" "success"}

# method: update
@app.post("/bot/message/update")
async def update_message(message: Message):
    list_message = read_data()
    # list_message = json.loads(list_message)
    for mess in list_message:
       if (mess["message_id"] == message.get_message_id() ):
           mess["message"] = message.get_message()
           break;
    # lưu vào file
    with open("data.json","w") as file:
        json.dump(list_message, file)

    return {"message": "success"}




    
    
    

        

