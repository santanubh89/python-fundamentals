import json


class Student():
    def __init__(self, id, name, score):
        self._id = id
        self._name = name
        self._score = score

    def __eq__(self, other):
        return self._id == other._id

    def __gt__(self, other):
        return self._score > other._score

    def __lt__(self, other):
        return self._score < other._score

    def __add__(self, other):
        return self._score + other._score

    def __str__(self):
        return json.dumps(self.__dict__)

    def __del__(self):
        print(f'Deleting {self._name}')
        self._name = ''
        self._score = 0
        self._id = None


alpha1 = Student('alpha', 'Foo Bar', 100)
beta = Student('beta', 'Bar Baz', 90)
alpha2 = Student('alpha', 'Foo', 100)

print(f'Alpha1 == Alpha2: {alpha1 == alpha2}')
print(f'Alpha > Beta: {alpha1 > beta}')

print(f'Sum of {alpha1._name} and {beta._name} is {alpha1 + beta}')

print(f'String form of object: {str(alpha1)}')

del alpha1