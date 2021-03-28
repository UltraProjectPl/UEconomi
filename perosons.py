from enum import Enum
from random import randint
from typing import Union


class Stuff(Enum):
    Food = "food"


class Person:
    NAME = "PERSON"

    def __init__(self, id: int, work: Stuff = None):
        self.id: int = id
        self.starving: int = 0
        self.work = work

    def hungry(self):
        self.starving += randint(1, 3)

    def working(self, efficiency_min: int = 0, efficiency_max: int = 0):
        return None


class Farmer(Person):
    NAME = "Farmer"

    def __init__(self, id: int):
        super().__init__(id, Stuff.Food)

    def working(self, efficiency_min: int = 1, efficiency_max: int = 2) -> int:
        return randint(efficiency_min, efficiency_max)
