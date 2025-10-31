import json
from time import time
from os import path, makedirs

ROOT_DIR = path.dirname(path.dirname(__file__))
CACHE_DIR = path.join(ROOT_DIR, ".cache")
CACHE_FILE = path.join(CACHE_DIR, "weather.json")
CACHE_EXP = 1800

def load_cache():
    # check if cache file exists, else return null dict
    if path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_cache(cache):
    makedirs(path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)

def is_valid_cache(entry):
    return time() - entry.get("timestamp", 0) < CACHE_EXP