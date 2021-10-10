import random


class CardList:
    def __init__(self, my_list):
        self.list = my_list

    def shuffle(self):
        random.shuffle(self.list)

    def add_card(self, card):
        self.list.append(card)
