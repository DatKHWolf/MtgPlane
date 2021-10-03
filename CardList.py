import random

class cardlist:
    def __init__(self, list):
        self.list=list

    def shuffle(self):
        random.shuffle(self.list)

    def addcard(self, card):
        self.list.append(card)



