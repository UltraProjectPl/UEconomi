from enum import Enum
from random import randint
from typing import Dict


class Stuff(Enum):
    Food = "food"


class Inventory:
    def __init__(self):
        self.stuffs: Dict[Stuff, float] = {stuff: 10 for stuff in Stuff}

    def get(self, stuff: Stuff) -> float:
        return self.stuffs[stuff]

    def add(self, stuff: Stuff, value: float):
        self.stuffs[stuff] += value

    def subtract(self, stuff: Stuff, value: float):
        self.stuffs[stuff] -= value


class Person:
    NAME = "PERSON"

    def __init__(self, id: int, work: Stuff = None):
        self.id: int = id
        self.money: float = 1000
        self.inventor: Inventory = Inventory()
        self.work = work

    def make_hungry(self):
        self.inventor.subtract(Stuff.Food, randint(1, 3))

    def working(self, efficiency_min: int = 0, efficiency_max: int = 0):
        return None

    def generate_need(self) -> Dict[Stuff, float]:
        return {stuff: self._how_need_stuff(stuff) for stuff in Stuff}

    def _how_need_stuff(self, stuff: Stuff) -> float:
        need = 100 - pow(self.inventor.get(stuff), 3)
        return need if need > 0 else 1


class Farmer(Person):
    NAME = "Farmer"

    def __init__(self, id: int):
        super().__init__(id, Stuff.Food)

    def working(self, efficiency_min: int = 3, efficiency_max: int = 10) -> float:
        return randint(efficiency_min, efficiency_max)

