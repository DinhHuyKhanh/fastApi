from bson.objectid import ObjectId
from pymongo import MongoClient
import json 

myClient = MongoClient("mongodb://localhost:27017/")
my_db = myClient["chatt"]

bot_col = my_db["bot"]
intent_col = my_db["intent"]
entity_col = my_db["entity"]


def find_all_bot(search: str,sort_type: str, field: str):
    list_bot=[]
   
    _sort={"asc":1, "desc":-1,"1":1,"-1":-1}

    if(_sort.get(sort_type) != None):
        sort_type=_sort.get(sort_type)
    else:
        sort_type=1

    for bot in bot_col.find({"name":{"$regex":search}}).sort(field,sort_type):
        list_bot.append({ "id": str(bot["_id"]) ,"name":bot["name"],"description":bot["description"],"enabled":bot["enabled"],
                    "config":bot["config"],"owner":bot["owner"] })
    return list_bot

def find_bot_by_id(bot_id: str):
    bot = bot_col.find_one({"_id": ObjectId(bot_id)})
    data= { "id": str(bot["_id"]) ,"name":bot["name"],"description":bot["description"],
            "enabled":bot["enabled"], "config":bot["config"],"owner":bot["owner"] }
    return data

def create_bot(bot: json):
    bot_col.insert_one(bot)
    return {"message":"success"}

def update_bot(bot_id: str , bot: json):
    bot_col.update_one({"_id":ObjectId(bot_id)}, {"$set": bot})
    return {"message":"success"}    

def delete_bot(bot_id: str):
    bot_col.delete_one({"_id":ObjectId(bot_id)})
    return {"message":"success"}



#lấy tất cả bot
# for bot in bot_col.find():
#     print(bot)

# lấy 1 document
# bot = bot_col.find_one();
# print("\n lấy 1 bot:")
# print(bot) 

#lấy tất cả document có keyword bot
# print("\n lay thong tin name theo key")
# for bot in bot_col.find({"name":{"$regex": "3"} }):
#     print(bot)


## lấy 1 document theo id
# bot = bot_col.find_one({"_id":ObjectId("619f46464d46e782bca7c931")})
# print(bot)


## lấy 2 document
# print("lấy 2 document bot")
# for bot in bot_col.find().limit(2).sort("name",-1):
#     print(bot)

##insert 1 object Id
# dict={"name": "bot demo", "description":"this is bot demo","enabled":True, "config":"auto"}
# bot_col.insert_one(dict)

##update 1 bot theo id
# bot_col.update({"_id":ObjectId("61a08fa9cd7d9254b0c3bb07")},
#                 {'$set':{"name":"bot demo update"} } )          

##delete 1 bot theo id
# bot_col.delete_one({"_id": ObjectId("61a08e99edc4de293aad71ba")})

## sắp xếp theo name theo asc
# print("sắp xếp theo asc")
# botList = bot_col.find().sort("name")
# for bot in botList :
#     print(bot)

## sắp xếp name theo desc
# print("sắp xếp theo desc") 
# botList = bot_col.find().sort("name",-1)
# for bot in botList :
#     print(bot)


##insert 1000 bot
# dict={"name": "bot demo", "description":"this is bot demo","enabled":True, "config":"auto"}
# int[1000]
# bot_col.insert_one(dict)

# bot = bot_col.find_one()
# print(str(bot["_id"]))




## insert 1000 document bot, entity, intent
## insert 1000 bot
# cnt=1000
# while(cnt):
#     dict_bot={"name": "bot demo", "description":"this is bot demo","enabled":True, "config":"auto","owner":""}
#     name= "bot demo "+str(cnt) 
#     description="this is bot demo " + str(cnt)
#     dict_bot['name']=name
#     dict_bot['description'] = description
#     bot_col.insert_one(dict_bot)
#     cnt-=1


# count = 1000
# while(count):
#     cnt=1000
#     while(cnt):
#         bot=bot_col.find_one({"name":"bot demo "+str(cnt)})
#         bot_id = str(bot['_id'])

#         dict_entity ={"name":"","bg_color":"red","fg_color":"C00000","bot":bot_id}
#         dict_entity["name"]="entity "+ str(count) + " of bot "+str(cnt)
#         entity_col.insert_one(dict_entity)

#         dict_intent ={"name":"","description":"","bot":bot_id}
#         dict_intent["name"]="intent "+ str(count) + " of bot "+str(cnt) 
#         dict_intent["description"] = "this is intent "+str(count) + "of bot "+str(cnt) 
#         intent_col.insert_one(dict_intent)
#         cnt-=1
#     count-=1

# tạo chỉ mục đơn của entity
# reps= entity_col.create_index([("bot",1)])
# print(reps)

# xóa index
# reps = entity_col.drop_index([("bot",1)])
# print(reps)
## tạo chỉ mục đơn của intent bot
# reps = intent_col.create_index([("bot",1)])
# print(reps)


# tìm tất cả entity của bot 1000

# bot_id="61a0b47f24140ca79113ab86"

# print("entity")
# for entity in entity_col.find({"bot":bot_id}):
#     print(entity);

# print("intent : ")
# for intent in intent_col.find({"bot":bot_id}):
#     print(intent)

# bot = bot_col.find_one({"name":"bot demo 999"})
# bot_id = str(bot["_id"])1

# entity = entity_col.find_one({"bot":bot_id})
# intent = intent_col.find_one({"bot":bot_id})
# print("\n bot:",bot)
# print("\n entity :",entity)
# print("\n intent: ", intent)




# bot_col.delete_many({})
# entity_col.delete_many({})
# intent_col.delete_many({})


    
    

    



    


