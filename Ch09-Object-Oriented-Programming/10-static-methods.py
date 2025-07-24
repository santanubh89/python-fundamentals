class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show(self):
        print(f'Username: {self.username} | Password: {self.password}')

    @staticmethod
    def jsonify(user):
        return {
            'username': user.username,
            'password': user.password
        }

user = UserData('Foo', 'Secret')
user.show()
# static method
json = UserData.jsonify(user)
print(f'Object: {json}')