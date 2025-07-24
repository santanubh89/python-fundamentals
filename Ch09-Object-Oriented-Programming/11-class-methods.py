from tkinter.font import names


class Employee:
    company = 'Google'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'Name: {self.name}, Company: {self.company}')

    @classmethod # changes on class level
    def change_company(clazz, new_company):
        clazz.company = new_company

e1 = Employee('Foo')
e1.show()

e1.change_company('Apple')
e1.show()
print(f'Company Name: {Employee.company}')

