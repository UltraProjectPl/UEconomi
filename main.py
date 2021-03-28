from typing import List
from time import sleep
from random import randint


class Person:
    def __init__(self, id: int):
        self.id: int = id
        self.starving: int = 0

    def hungry(self):
        self.starving += randint(1, 3)


def showPersons(persons: List[Person]):
    for person in persons:
        print("""
            Person:
               Id: {}
               Starving: {}
        """.format(person.id, person.starving))


persons: List[Person] = []
for i in range(5):
    persons.append(Person(i))


for _ in range(10):
    for person in persons:
        person.hungry()
        if person.starving > 10:
            persons.remove(person)
    showPersons(persons)
    sleep(1)


print("===============================END==========================================")
showPersons(persons)
