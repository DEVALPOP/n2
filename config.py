import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21769847))

    API_HASH = os.environ.get("API_HASH", "d5031334164f12ef47a7f3c7c3116207")
