# Write a class to hold player information, e.g. what room they are in
# currently.

# if these are marked as None, I dont have to declare them on the main page

class Player:
    def __init__(self, current_room=None):
        # self.name = name
        self.current_room = current_room

    # def__str__(self):
    #     return f"{self.name}: {self.current_room}"
