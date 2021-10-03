from flask import Flask, render_template, url_for
import requests
import random
from CardList import cardlist
from Card import Card


app = Flask(__name__)


@app.route("/")
def get_planes():
    my_list = cardlist([])
    url = 'https://api.scryfall.com/cards/search?q=t%3Aplane'
    req = requests.get(url)
    card_list = req.json()['data']
    split_phrase = 'Whenever you roll {CHAOS}'

    for card in card_list:

        name = (card['name'])
        text = (card['oracle_text'])
        oracle_text = text.split(split_phrase)[0]
        chaos_text = split_phrase + text.split(split_phrase)[1]
        image = (card['image_uris']['border_crop'])
        rulings = card['rulings_uri']

        plane = Card(name, oracle_text, chaos_text, image, rulings)
        my_list.addcard(plane)
        my_list.shuffle()

        # TODO: Karte in DB speichern

    return render_template('index.html', cards=my_list.list)


if __name__ == '__main__':
    app.run()
