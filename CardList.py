import random


class CardList:
    def __init__(self, my_list):
        self.list = my_list
        self.list_position = 0

    def shuffle(self):
        random.shuffle(self.list)

    def add_card(self, card):
        self.list.append(card)

    def current_card(self):
        return self.list[self.list_position]

    def next_card(self):
        self.list_position += 1
        # print(self.list_position)
        return self.list[self.list_position]
    # TODO: Index out of bounds abfangen

    def prev_card(self):
        self.list_position -= 1
        # print(self.list_position)
        return self.list[self.list_position]

    def print_list(self):
        counter = 0
        for card in self.list:

            print("Listposition : ")
            print(counter)
            print(" ist die Position von Karte :")
            print(card.name)

            counter += 1


