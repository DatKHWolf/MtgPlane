from flask import Flask, render_template
from CardList import CardList
from Card import Card
from random import randint
import requests

app = Flask(__name__)

# Als init auslagern ...

SCRYFALL_PLANES_URL = 'https://api.scryfall.com/cards/search?q=type%3Aphenomenon+OR+type%3Aplane'
ORACLE_SPLIT_PHRASE = 'Whenever you roll {CHAOS}'

req = requests.get(SCRYFALL_PLANES_URL)
scryfall_list = req.json()['data']
my_planes = CardList([])

for card in scryfall_list:
    name = (card['name'])
    type_line = (card['type_line'])
    text = (card['oracle_text'])
    image = (card['image_uris'])     # png, border_crop, art_crop, large, normal, small
    rulings = card['rulings_uri']

    if card['type_line'] == 'Phenomenon':
        oracle_text = text
        chaos_text = ''
    else:
        oracle_text = text.split(ORACLE_SPLIT_PHRASE)[0]
        chaos_text = ORACLE_SPLIT_PHRASE + text.split(ORACLE_SPLIT_PHRASE)[1]

    plane = Card(name, type_line, oracle_text,
                 chaos_text, image, rulings)
    my_planes.add_card(plane)

my_planes.shuffle()
# my_planes.print_list()

@app.route("/", methods=['POST', 'GET'])
def start_screen():
    return render_template('index.html')

@app.route("/play", methods=['POST', 'GET'])
def play():
    return render_template('play.html', card=my_planes.current_card())

@app.route("/allcards", methods=['GET'])
def show_planes():
    return render_template('allcards.html', cards=my_planes.list)

@app.route("/nextcard", methods=['GET'])
def next_card():
    return render_template('play.html', card=my_planes.next_card())

@app.route("/prevcard", methods=['GET'])
def prev_card():
    return render_template('play.html', card=my_planes.prev_card())

@app.route("/dice", methods=['POST'])
def roll_dice():
    dice_value = randint(1, 6)       #Planechase Würfel..
    return render_template('play.html', card=my_planes.current_card(), result=dice_value)


if __name__ == '__main__':
    app.run()
