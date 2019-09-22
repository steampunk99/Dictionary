import json
from difflib import get_close_matches

data = json.load(open("data/data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    else:
        return "This word is not in this dictionary"


word = input("Enter a word: ")

output = translate(word)
if output == string:
    for item in output:
        print(item)

else:
    print(item)
