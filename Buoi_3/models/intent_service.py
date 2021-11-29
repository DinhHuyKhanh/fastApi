from bson.objectid import ObjectId
from pymongo import MongoClient
import json

myClient = MongoClient("mongodb://localhost:27017/")
my_db = myClient["chatt"]

intent_col = my_db["intent"]

def get_intent_by_bot_id(bot_id: str):
    list_intent=[]
    for intent in intent_col.find({"bot": bot_id }):
        list_intent.append({"id": str(intent["_id"]), "name":intent["name"],"description":intent["description"]})
    return list_intent

def create_intent(intent: json):
    intent_col.insert_one(intent)
    return {"message":"success"}

def update_intent(intent_id: str , intent: json):
    intent_col.update_one({"_id":ObjectId(intent_id)}, {"$set": intent})
    return {"message":"success"}    

def delete_intent(intent_id: str):
    intent_col.delete_one({"_id":ObjectId(intent_id)})
    return {"message":"success"}