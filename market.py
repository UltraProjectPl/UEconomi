from perosons import Stuff


class Market:
    def __init__(self):
        self.stuffs = {stuff: 0 for stuff in Stuff}

    def add_stuff(self, stuff: Stuff, quantity: int):
        self.stuffs[stuff] += quantity
