# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.w_to = None
        self.s_to = None
        self.e_to = None
        self.loot = []

    def __str__(self):
        output = f'{self.name}: {self.description}\n'
        if self.n_to:
            output += 'To the north is: ' + self.n_to.name + '\n'
        if self.e_to:
            output += 'To the east is: ' + self.e_to.name + '\n'
        if self.s_to:
            output += 'To the south is: ' + self.s_to.name + '\n'
        if self.w_to:
            output += 'To the west is: ' + self.w_to.name + '\n'

        return output

    def add_item(self, item):
        self.loot.append(item)

    def remove_item(self, item):
        self.loot.remove(item)

    def show_items(self):
        for item in self.loot:
            return f"There is an item in the room. {item.name}: {item.description}"
