from bson.objectid import ObjectId
from pymongo import MongoClient
import json

myClient = MongoClient("mongodb://localhost:27017/")
my_db = myClient["chatt"]

entity_col = my_db["entity"]

def get_entity_by_bot_id(bot_id: str):
    list_entity=[]
    for entity in entity_col.find({"bot": bot_id }):
        list_entity.append({"id": str(entity["_id"]), "name":entity["name"],"bg_color":entity["bg_color"],"fg_color":entity["fg_color"]})
    return list_entity

def create_entity(entity: json):
    entity_col.insert_one(entity)
    return {"message":"success"}

def update_entity(entity_id: str , entity: json):
    entity_col.update_one({"_id":ObjectId(entity_id)}, {"$set": entity})
    return {"message":"success"}    

def delete_entity(entity_id: str):
    entity_col.delete_one({"_id":ObjectId(entity_id)})
    return {"message":"success"}