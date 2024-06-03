import oracledb
from sqlalchemy import create_engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils.db_service import init_db_and_create_tables, init_db
from config.app_config import web_app
from routes import public_api_route 

if __name__ == '__main__':
    init_db()
    web_app.run(debug=True)