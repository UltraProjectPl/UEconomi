from typing import List
from time import sleep
from random import randint
from enum import Enum


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


class Farmer(Person):
    NAME = "Farmer"

    def __init__(self, id: int):
        super().__init__(id, Stuff.Food)


def showPersons(persons: List[Person]):
    for person in persons:
        print("""
            {}:
               Id: {}
               Starving: {}
        """.format(person.NAME, person.id, person.starving))


persons: List[Person] = []
for i in range(5):
    persons.append(Person(i))

for i in range(3):
    persons.append(Farmer(i + 5))

for _ in range(10):
    for person in persons:
        person.hungry()
        if person.starving > 10:
            persons.remove(person)
    showPersons(persons)
    sleep(1)


print("===============================END==========================================")
showPersons(persons)
