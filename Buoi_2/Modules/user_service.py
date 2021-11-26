
import json
from fastapi.encoders import jsonable_encoder
from typing import List
from Modules.user import User

class user_service:

    def read_users():
        with open("user.json","r") as file:
            list_users = json.load(file)
        return list_users;

    def save_user(user : User ):
        list_users = user_service.read_users()

        user.set_user_id( user_id=len(list_users) + 1)
        data = jsonable_encoder(user)

        for u in list_users :
            if u.get("username") == user.username : 
                return {"message":"User already exists"}

        list_users.append(data)
        with open("user.json","w") as file:
            json.dump(list_users, file)

        return {"message":"success"}
