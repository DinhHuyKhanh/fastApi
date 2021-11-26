from fastapi import FastAPI
import models.bot_service 
from modules.bot import Bot

app = FastAPI()

@app.get('/bot')
def get_all_bot():
    return models.bot_service.get_all_bot()

@app.post("/bot")
def create_bot(bot: Bot):
    return models.bot_service.insert_bot(Bot)


