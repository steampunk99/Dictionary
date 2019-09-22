import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return w[data]

    else:
        return "This word is not in this dictionary"

word = input("Enter a word: ")

output = translate(word)