from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
import models.bot_service
import models.entity_service
import models.intent_service
from modules.bot import Bot
from modules.entity import Entity
from modules.intent import Intent

app = FastAPI()

@app.get('/bot')
def get_all_bot(search:str = Query('',max_length=10), sort_type: str= Query("asc",max_length=4), field: str=Query("name",max_length=20)):
    return models.bot_service.find_all_bot(search=search, sort_type=sort_type, field=field)

@app.get("/bot/{bot_id}")
def get_bot_by_id(bot_id: str):
    return models.bot_service.find_bot_by_id(bot_id=bot_id)

@app.post("/bot")
def create_bot(bot: Bot):
    data = jsonable_encoder(bot)
    return models.bot_service.create_bot(data)

@app.put("/bot/{bot_id}")
def update_bot(bot_id: str ,bot:Bot):
    data = jsonable_encoder(bot)
    return models.bot_service.update_bot(bot_id=bot_id, bot=data)

@app.delete("/bot/{bot_id}")
def delete_bot(bot_id: str):
    return models.bot_service.delete_bot(bot_id=bot_id)


@app.get("/entity/{bot_id}")
def get_all_entity_by_bot_id(bot_id: str):
    return models.entity_service.get_entity_by_bot_id(bot_id=bot_id)

@app.post("/entity")
def create_entity(entity : Entity):
    data = jsonable_encoder(entity)
    return models.entity_service.create_entity(data)

@app.put("/entity/{entity_id}")
def update_entity(entity_id: str,entity: Entity):
    data = jsonable_encoder(entity)
    return models.entity_service.update_entity(entity_id=entity_id, entity=data)

@app.delete("/entity/{entity_id}")
def delete_entity(entity_id: str):
    return models.entity_service.delete_entity(entity_id=entity_id)


@app.get("/intent/{bot_id}")
def get_all_intent_by_bot_id(bot_id: str):
    return models.intent_service.get_intent_by_bot_id(bot_id=bot_id)

@app.post("/intent")
def create_intent(intent : Intent):
    data = jsonable_encoder(intent)
    return models.intent_service.create_intent(data)

@app.put("/intent/{intent_id}")
def update_intent(intent_id: str,intent: Intent):
    data = jsonable_encoder(intent)
    return models.intent_service.update_intent(intent_id=intent_id, intent=data)

@app.delete("/intent/{intent_id}")
def delete_intent(intent_id: str):
    return models.intent_service.delete_intent(intent_id=intent_id)





    


