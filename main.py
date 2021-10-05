from flask import Flask, render_template
from CardList import CardList
from Card import Card
import requests


app = Flask(__name__)

SCRYFALL_PLANES_URL = 'https://api.scryfall.com/cards/search?q=t%3Aplane'
ORACLE_SPLIT_PHRASE = 'Whenever you roll {CHAOS}'

# Hole alle Karten mit typ:plane von Scryfall und pack sie in 'ne Liste
my_planes = CardList([])
req = requests.get(SCRYFALL_PLANES_URL)
card_list = req.json()['data']

# Speichere für jede Karte nur die relevanten Infos ab
for card in card_list:
    name = (card['name'])
    text = (card['oracle_text'])
    oracle_text = text.split(ORACLE_SPLIT_PHRASE)[0]
    chaos_text = ORACLE_SPLIT_PHRASE + text.split(ORACLE_SPLIT_PHRASE)[1]
    image = (card['image_uris']['border_crop'])
    rulings = card['rulings_uri']

    plane = Card(name, oracle_text, chaos_text, image, rulings)
    my_planes.add_card(plane)


@app.route("/")
def show_planes():
    return render_template('index.html', cards=my_planes)


@app.route("/shuffle")
def shuffle():
    my_planes.shuffle()
    return render_template('index.html', cards=my_planes)


if __name__ == '__main__':
    app.run()
