from flask import Flask, render_template, url_for
import requests
import random
from CardList import cardlist


app = Flask(__name__)
my_list = cardlist([])

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

@app.route("/")
def get_planes():
    url = 'https://api.scryfall.com/cards/search?q=t%3Aplane'
    req = requests.get(url)
    card_list = req.json()['data']
    for card in card_list:
        plane = Card((card['name']), card['oracle_text'], card['image_uris']['border_crop'], card['rulings_uri'])
        # TODO: Karte in DB speichern
        my_list.addcard(plane)
        my_list.shuffle()
    return render_template('index.html', cards = my_list.list)

if __name__ == '__main__':
    app.run()