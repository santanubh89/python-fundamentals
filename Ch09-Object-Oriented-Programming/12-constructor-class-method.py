class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_data(clazz, string):
        name, salary = string.split('#')
        return clazz(name, int(salary))


e1 = Employee('Foo', 25000)
print(f'Name: {e1.name}, Salary: {e1.salary}')

emp_data = 'Foo#25000'
e2 = Employee.from_data(emp_data)
print(f'Name: {e2.name}, Salary: {e2.salary}')