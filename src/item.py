class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def take(self):
        print(f"\nYou have picked up a {self.name}. {self.description}")

    def drop(self):
        print(f"\nYou have dropped {self.name}")
