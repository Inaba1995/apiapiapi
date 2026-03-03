import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
YANDEX_WEATHER_KEY = os.getenv("YANDEX_WEATHER_API_KEY")
CB_API_URL = os.getenv("CB_API_URL")



if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в ..env файле!")
