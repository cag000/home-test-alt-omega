import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from dotenv import load_dotenv

Base = declarative_base()

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECONDARY_DATABASE_URL = os.getenv("SECONDARY_DATABASE_URL")


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PrimaryDatabase(metaclass=SingletonMeta):
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        self.Base = declarative_base()


# Instantiate the singleton
db_engine = PrimaryDatabase()

# Raw SQL Database connection
primary_database = Database(DATABASE_URL)
secondary_database = Database(SECONDARY_DATABASE_URL)
