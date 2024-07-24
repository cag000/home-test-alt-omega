import os
from dotenv import load_dotenv

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class EnvLoader(metaclass=SingletonMeta):
    def __init__(self, dotenv_path: str = ".env"):
        load_dotenv(dotenv_path)
        self.env = os.environ

    def get(self, key: str, default: str = None) -> str:
        return self.env.get(key, default)
