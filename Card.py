class Card:
    def __init__(self, name, oracle_text, chaos_text, image, rules):
        self.name = name
        self.oracle_text = oracle_text
        self.chaos_text = chaos_text
        self.image = image
        self.rules = rules

    # Testen
    def print_name(self):
        print(self.name)

    def print_chaos_text(self):
        print(self.chaos_text)

    def print_oracle_text(self):
        print(self.oracle_text)

    def print_image(self):
        print(self.image)
