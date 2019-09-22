import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))

def translate(w):
    if w in data:
        