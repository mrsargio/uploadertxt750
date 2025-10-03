#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24250238"))
API_HASH = environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")
BOT_TOKEN = environ.get("BOT_TOKEN", "6234022831:AAGXxnk_pOGRm0dUAFPQHjgF9h2vEtdzGTs")
OWNER = int(environ.get("OWNER", "6175650047"))
CREDIT = "Sargio"
LOG_CHANNEL = "-1003164620330" # log group me bot ko admin narur banaye full rights ke sath
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

