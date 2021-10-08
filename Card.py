class Card:
    def __init__(self, name, type_line, oracle_text, chaos_text, image, rules):
        self.name = name
        self.type_line = type_line
        self.oracle_text = oracle_text
        self.chaos_text = chaos_text
        self.image = image
        self.rules = rules

    def print_name(self):
        print(self.name)

    def print_chaos_text(self):
        print(self.chaos_text)

    def print_oracle_text(self):
        print(self.oracle_text)

    def print_image(self):
        print(self.image)
