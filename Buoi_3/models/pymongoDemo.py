from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["chatt"]
mycol = mydb["bot"]

x= mycol.find_one()
for i in mycol.find() :
    print(i);
