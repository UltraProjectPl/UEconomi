from enum import Enum
from random import randint


class Stuff(Enum):
    Food = "food"


class Person:
    NAME = "PERSON"

    def __init__(self, id: int, work: Stuff = None):
        self.id: int = id
        self.money: float = 1000
        self.starving: int = 0
        self.work = work

    def hungry(self):
        self.starving += randint(1, 3)

    def working(self, efficiency_min: int = 0, efficiency_max: int = 0):
        return None

    def buy_stuff_consider(self, value: float) -> bool:
        if 0 < self.starving:
            return pow(self.starving, 2) <= (self.money / value) * 100
        return False


class Farmer(Person):
    NAME = "Farmer"

    def __init__(self, id: int):
        super().__init__(id, Stuff.Food)

    def working(self, efficiency_min: int = 1, efficiency_max: int = 2) -> float:
        return randint(efficiency_min, efficiency_max)

