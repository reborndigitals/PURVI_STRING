from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","8045459"))
API_HASH = getenv("API_HASH","e6d1f09120e17a4372fe022dde88511b")

BOT_TOKEN = getenv("BOT_TOKEN", "2132260441:AAEGAiQWe8lq-O6IvoWoY-4BROsoqxiPc-E")
OWNER_ID = int(getenv("OWNER_ID","1281282633"))

MONGO_DB_URI = getenv("mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","HeartBeat_Muzic")
