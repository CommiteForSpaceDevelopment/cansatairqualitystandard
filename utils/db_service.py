import oracledb
from sqlalchemy import create_engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from models.schemas import Base
import logging
from config.db_config import Db_config

def init_db():
    db_config = Db_config()
    con = oracledb.connect(user=db_config.db_user,password=db_config.db_password, dsn=db_config.db_con)
    engine = create_engine(f"oracle+oracledb://{db_config.db_user}:{db_config.db_password}@{db_config.db_con}")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def init_db_and_create_tables():
    db_config = Db_config()
    logging.basicConfig(level=logging.DEBUG)  
    logger = logging.getLogger(__name__)
    logger.info("Initializing database and creating tables...")
    con = oracledb.connect(user=db_config.db_user,password=db_config.db_password, dsn=db_config.db_con)
    engine = create_engine(f"oracle+oracledb://{db_config.db_user}:{db_config.db_password}@{db_config.db_con}")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    return Session()