from typing import List
from time import sleep
from perosons import Person, Farmer, Stuff
from market import Market
import pprint

def show_persons(persons: List[Person]):
    for person in persons:
        print(f"""
        {person.NAME}_{person.id}:
            Money: {person.money},
            Inventor:
                {Stuff.Food}: {person.inventor.get(Stuff.Food)}
        """)


persons: List[Person] = []
for i in range(5):
    persons.append(Person(i))

for i in range(3):
    persons.append(Farmer(i + 5))


market = Market()

for _ in range(10):
    for person in persons:
        person.inventor.subtract(Stuff.Food, 1)

        needs = person.generate_need()

        for stuff, need in needs.items():
            if 0 < market.get_stuff_quantity(stuff) and person.money >= market.get_stuff_value(stuff):
                if (person.money * (need / 100)) >= market.get_stuff_value(stuff):
                    food = market.sell_stuff(Stuff.Food)
                    person.money = round(person.money - market.market[Stuff.Food]["value"], 2)
                    person.inventor.add(Stuff.Food, food)

        if person.work:
            payout: float = market.buy_stuff(person.work, person.working())
            person.money = round(person.money + payout, 2)
        if 0 >= person.inventor.get(Stuff.Food):
            persons.remove(person)
    # sleep(1)

show_persons(persons)
pprint.pprint(market.market)