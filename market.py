from perosons import Stuff, Person
from typing import Dict



class Market:
    def __init__(self):
        self.market: Dict[Stuff, Dict[str, float]] = {
            stuff: {
                "value": 1,
                "quantity": 0
            } for stuff in Stuff
        }

    def get_stuff_value(self, stuff: Stuff):
        return self.market[stuff]["value"]

    def get_stuff_quantity(self, stuff: Stuff):
        return self.market[stuff]["quantity"]

    def buy_stuff(self, stuff: Stuff, quantity: float) -> float:
        if 0 < self.get_stuff_quantity(stuff) and 1 > self.get_stuff_value(stuff):
            self.edit_value_stuff(stuff, -(quantity / self.get_stuff_quantity(stuff)) * self.get_stuff_value(stuff))
        self.market[stuff]["quantity"] += quantity
        return round(self.get_stuff_value(stuff) * quantity, 2)

    def sell_stuff(self, stuff: Stuff) -> float:
        if 0 < self.get_stuff_quantity(stuff):
            self.edit_value_stuff(stuff, (1 / self.get_stuff_quantity(stuff)) * self.get_stuff_value(stuff))
        self.market[stuff]["quantity"] -= 1
        return 1.0

    def edit_value_stuff(self, stuff: Stuff, value: float):
        self.market[stuff]["value"] += value
        self.market[stuff]["value"] = round(self.market[stuff]["value"], 2)