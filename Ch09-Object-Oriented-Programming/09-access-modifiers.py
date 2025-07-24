class UserData:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self._role = 'Admin'

    def show(self):
        print(f'Object: {self.__dict__}')

user = UserData('Foo', 'Secret')
user.show()
print(f'Username is public: {user.username}')
#print(f'Password is private: {user.__password}')
print(f'Accessing private variable: {user._UserData__password}')
print(f'Accessing protected variable: {user._role}')