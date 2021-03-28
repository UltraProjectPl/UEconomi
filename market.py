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

    def buy_stuff(self, stuff: Stuff, quantity: float) -> float:
        if 0 < self.market[stuff]["quantity"] and 1 < self.market[stuff]["value"]:
            self.market[stuff]["value"] -= (quantity / self.market[stuff]["quantity"]) * self.market[stuff]["value"]
        self.market[stuff]["quantity"] += quantity
        return self.market[stuff]["value"] * quantity

    def sell_stuff(self, stuff: Stuff) -> float:
        if 0 < self.market[stuff]["quantity"] and 1 < self.market[stuff]["value"]:
            self.market[stuff]["value"] += (1 / self.market[stuff]["quantity"]) * self.market[stuff]["value"]
        self.market[stuff]["quantity"] -= 1
        return 1