import random


class CardList(list):
    def __init__(self, mylist):
        super().__init__()
        self.list = mylist

    def shuffle(self):
        random.shuffle(self.list)

    def addcard(self, card):
        self.list.append(card)

