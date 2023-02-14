# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "16445683"))
API_HASH = os.environ.get("API_HASH", "d0852e13eee2389ff2d9183b00649547")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6052097137:AAFtACerJO2nfkNfTk_3bhiiRhBqw5Csx5c")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5628615681")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "SawanSingh")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://SawanSingh:sawansingh@cluster0.h2prshr.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5628615681")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5628615681)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001811438803")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdisklinkonline") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
