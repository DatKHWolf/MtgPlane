from flask import Flask, render_template
import requests
from CardList import CardList
from Card import Card

app = Flask(__name__)

# Hole alle Karten mit typ:plane von Scryfall und pack sie in 'ne Liste
my_planes = CardList([])
url = 'https://api.scryfall.com/cards/search?q=t%3Aplane'
req = requests.get(url)
card_list = req.json()['data']
split_phrase = 'Whenever you roll {CHAOS}'

# Speichere für jede Karte nur die relevanten Infos ab
for card in card_list:
    name = (card['name'])
    text = (card['oracle_text'])
    oracle_text = text.split(split_phrase)[0]
    chaos_text = split_phrase + text.split(split_phrase)[1]
    image = (card['image_uris']['border_crop'])
    rulings = card['rulings_uri']

    plane = Card(name, oracle_text, chaos_text, image, rulings)
    my_planes.addcard(plane)

@app.route("/")
def show_planes():
    return render_template('index.html', cards=my_planes)


@app.route("/shuffle")
def shuffle():
    my_planes.shuffle()
    return render_template('index.html', cards=my_planes)


if __name__ == '__main__':
    app.run()
