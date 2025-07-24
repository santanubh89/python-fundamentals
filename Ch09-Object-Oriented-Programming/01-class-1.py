class Person:
    name = 'Foo'
    occupation = 'Software Engineer'
    experience = 10
    def info(self):
        print(f'{self.name} has {self.experience} years of experience as {self.occupation}')

foo = Person()
print(f'Name of Person: {foo.name}')
foo.experience = 20
foo.info()