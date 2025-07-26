class UserData:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Employee:
    def __init__(self, emp_id, grade):
        self.emp_id = emp_id
        self.grade = grade

    def info(self):
        print(f'Employee ID: {self.emp_id}, Grade: {self.grade}')

class InternEmployee(UserData, Employee):
    def __init__(self, emp_id, grade):
        super().__init__(emp_id, grade)

internal_employee = InternEmployee('E123', 1)
print(internal_employee.info())