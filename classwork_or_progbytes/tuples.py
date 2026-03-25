from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

person1 = Person(name='Alice', age=25)
person2 = Person(name='Bob', age=30)
person3 = Person(name='Charlie', age=35)
person4 = Person(name='David', age=40)
person5 = Person(name='Eve', age=45)

people = [person1, person2, person3, person4, person5]

for i in range(len(people)):
    print(people[i].name)
