class Person:
    def __init__(self, name = '', age = 0, city = ''):
        self._name = name
        self._age = age
        self._city = city

    @property
    def name(self):
        print(f'Getter for Name called')
        return self._name

    @name.setter
    def name(self, name):
        print(f'Setter for Name called with value: {name}')
        self._name = name


p = Person('Foo Bar', 30, 'USA')
print(f'Name of Person: {p.name}')

p.name = 'Bar Baz'
print(f'Name of Person: {p.name}')