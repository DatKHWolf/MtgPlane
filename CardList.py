import random


class CardList(list):
    def __init__(self, my_list):
        super().__init__()
        self.list = my_list

    def shuffle(self):
        random.shuffle(self.list)

    def add_card(self, card):
        self.list.append(card)