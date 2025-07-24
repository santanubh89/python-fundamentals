list = [1, 2, 3]

# dir - prints list of attributes and methods in an object
dir_result = dir(list)
print(f'dir:\n{dir_result}')

class Employee:

    company = 'Google'

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def show(self):
        print(f'Name: {self.name}, Salary: {self.salary}')

e = Employee(1, 'Foo', 25000)
# dict - prints dictionary version of an object
obj_dict = e.__dict__
print(f'dict:\n{obj_dict}')
print(f'Name: {obj_dict['name']}')

# help - documents attributes and methods
print(help(Employee))