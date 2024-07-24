import redis
import os
from app.common.custom_errors import CacheError


class RedisCache:
    def __init__(self):
        try:
            self.client = redis.Redis(
                host=os.getenv("REDIS_HOST", "localhost"),
                port=int(os.getenv("REDIS_PORT", 6379)),
                db=int(os.getenv("REDIS_DB", 0)),
            )
        except redis.RedisError as e:
            raise CacheError(f"Failed to connect to Redis: {str(e)}")

    def get(self, key):
        try:
            return self.client.get(key)
        except redis.RedisError as e:
            raise CacheError(f"Failed to get key {key}: {str(e)}")

    def set(self, key, value, ex=None):
        try:
            self.client.set(key, value, ex=ex)
        except redis.RedisError as e:
            raise CacheError(f"Failed to set key {key}: {str(e)}")

    def delete(self, key):
        try:
            self.client.delete(key)
        except redis.RedisError as e:
            raise CacheError(f"Failed to delete key {key}: {str(e)}")
