from typing import List
import json

class utils:

    def read_users():
        with open("user.json","r") as file:
            list_users = json.load(file)
        return list_users;

    def save_user(list_users: List):
        with open("user.json","w") as file:
            json.dump(list_users, file)
    
    def read_message():
        with open("message.json","r") as file:
            list_message = json.load(file)
        return list_message;

    def save_message(list_message: List):
        with open("message.json","w") as file:
            json.dump(list_message, file)
    
            
    
