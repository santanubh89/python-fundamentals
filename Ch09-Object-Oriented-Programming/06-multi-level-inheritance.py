class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f'UserData::Login ==> Logging in with username: {self.username}')

class Employee(UserData):
    def __init__(self, username, password, emp_id, grade):
        super().__init__(username, password)
        self.emp_id = emp_id
        self.grade = grade

    def work(self):
        print(f'Employee::work ==> Working as per grade: {self.grade}')

class InternEmployee(Employee):
    def __init__(self, username, password, emp_id, grade, internship_period):
        super().__init__(username, password, emp_id, grade)
        self.internship_period = internship_period

    def report(self):
        print(f'InternEmployee::report ==> Internship period: {self.internship_period}')

intern = InternEmployee('Foo', 'Secret', 'Emp123', 8, 3)
print(f'Intern details:: {intern.__dict__}')
intern.login()
intern.work()
intern.report()
