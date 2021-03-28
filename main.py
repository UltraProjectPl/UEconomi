from typing import List


class Person:
    pass


persons: List[Person] = []
for _ in range(5):
    persons.append(Person())


for person in persons:
    print(person)