from dotenv import load_dotenv
import os

class Db_config():
    def __init__(self):
        env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.env"))
        print("ENV PATH "+env_path)
        load_dotenv(dotenv_path=env_path)
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_con = os.getenv("DB_CON")