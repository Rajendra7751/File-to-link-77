import os

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    DB_URI = os.getenv("DB_URI")
    PORT = int(os.getenv("PORT", 8080))
