import json


class Student():
    def __init__(self, id, name, score):
        self._id = id
        self._name = name
        self._score = score

    def __len__(self):
        return len(self._name)

    def __eq__(self, other):
        return self._id == other._id

    def __gt__(self, other):
        return self._score > other._score

    def __lt__(self, other):
        return self._score < other._score

    def __add__(self, other):
        return self._score + other._score

    def __call__(self, *args, **kwargs):
        print(f'Student object {self._name} called with args: {args}, kwargs: {kwargs}')

    def __strx__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return f'Student({self._id}, {self._name}, {self._score})'

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

print(f'Student: {alpha1}')

print(f'Length of Alpha: {len(alpha1)}')

alpha1(10, 20, age=12, school='ABC')

del alpha1