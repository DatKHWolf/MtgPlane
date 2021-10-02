from flask import Flask
from flask import request
import json
import requests

app = Flask(__name__)
unsere_liste = []

class Card:
    def __init__(self, name, text, image, rules):
        self.name=name
        self.text=text
        self.image=image
        self.rules=rules

# Testen
    def print_name(self):
        print(self.name)
    def print_text(self):
        print(self.text)
    def print_image(self):
        print(self.image)

def get_planes():
    url = 'https://api.scryfall.com/cards/search?q=t%3Aplane'
    res = requests.get(url)
    card_list = res.json()['data']
    for x in card_list:
        karte = Card((x['name']), x['oracle_text'], x['image_uris']['large'], x['rulings_uri'])

        unsere_liste.append(karte)
    return res.json()

get_planes()

for x in unsere_liste:
    x.print_name()
    x.print_text()
    x.print_image()
if __name__ == '__main__':
    app.run()