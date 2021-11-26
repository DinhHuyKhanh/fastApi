# from bson.objectid import ObjectId
from pymongo import MongoClient

myClient = MongoClient("mongodb://localhost:27017/")
my_db = myClient["chatt"]

bot_col = my_db["bot"]
intent_col = my_db["intent"]
entity_col = my_db["entity"]


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
# cnt=1000;
# while(cnt):
#     dict_bot={"name": "bot demo", "description":"this is bot demo","enabled":True, "config":"auto","owner":""}
#     name= "bot demo "+str(cnt) 
#     description="this is bot demo " + str(cnt)
#     dict_bot['name']=name
#     dict_bot['description'] = description
#     bot_col.insert_one(dict_bot)

#     bot = bot_col.find_one({"name":name})
#     bot_id = str(bot['_id'])

#     dict_entity ={"name":"","bg_color":"red","fg_color":"C00000","bot":bot_id}
#     dict_entity["name"]="entity "+ str(cnt)
#     entity_col.insert_one(dict_entity)

#     dict_intent ={"name":"","description":"","bot":bot_id}
#     dict_intent["name"]="intent "+ str(cnt)
#     dict_intent["description"] = "this is intent "+str(cnt)
#     intent_col.insert_one(dict_intent)
#     cnt-=1


# tạo chỉ mục đơn của entity
# reps= entity_col.create_index([("bot")])
# print(reps)

## tạo chỉ mục đơn của intent bot
# reps = intent_col.create_index([("bot",1)])
# print(reps)


## 
bot = bot_col.find_one({"name":"bot demo 999"})
bot_id = str(bot["_id"])

entity = entity_col.find_one({"bot":bot_id})
intent = intent_col.find_one({"bot":bot_id})
print("\n bot:",bot)
print("\n entity :",entity)
print("\n intent: ", intent)




    
    

    



    


