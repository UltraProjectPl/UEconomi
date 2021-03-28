from typing import List
from time import sleep
from perosons import Person, Farmer
from market import Market


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


market = Market()

for _ in range(10):
    for person in persons:
        person.hungry()

        if person.work:
            market.add_stuff(person.work, person.working())
        if person.starving > 10:
            persons.remove(person)
    showPersons(persons)
    sleep(1)


print("===============================END==========================================")
showPersons(persons)
print("Market value")
print(market.stuffs)
