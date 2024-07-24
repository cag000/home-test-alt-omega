# app/infrastructure/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.common.env_loader import EnvLoader

env = EnvLoader()

DATABASE_URL = env.get("DATABASE_URL")
SECONDARY_DATABASE_URL = env.get("SECONDARY_DATABASE_URL")

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseEngine(metaclass=SingletonMeta):
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

# Instantiate the singleton
db_engine = DatabaseEngine()

# Raw SQL Database connection
primary_database = Database(DATABASE_URL)
secondary_database = Database(SECONDARY_DATABASE_URL)
