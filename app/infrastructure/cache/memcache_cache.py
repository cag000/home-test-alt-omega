import memcache
from dotenv import load_dotenv
import os

load_dotenv()

MEMCACHE_URL = os.getenv("MEMCACHE_URL")
memcache_client = memcache.Client([MEMCACHE_URL])

def get_cache(key):
    return memcache_client.get(key)

def set_cache(key, value):
    memcache_client.set(key, value)

def invalidate_cache(key):
    memcache_client.delete(key)
