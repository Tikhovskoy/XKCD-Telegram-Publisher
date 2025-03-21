import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    config = {
        "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN"),
        "TELEGRAM_CHANNEL_ID": os.getenv("TELEGRAM_CHANNEL_ID"),
        "FILES_DIR": os.getenv("FILES_DIR", "files")
    }
    return config
