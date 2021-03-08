class Person:
    def __init__(self, n, a, g):
        self.name = n
        self.age = a
        self.gender = g

def greet(person):
    if person.gender == 'M' and person.age < 18:
        title = 'Master'
    elif person.gender == 'M':
        title = 'Mr.'
    else:
        title = 'Ms.'
    return f"Hello {title} {person.name}"

wayne = Person(n = 'Wayne', a = 16, g = 'M')
print(greet(wayne))