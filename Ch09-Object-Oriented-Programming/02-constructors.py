import json

class UserData:
    def __init__(self, name = '', age = None, city = 'unknown'):
        self.name = name
        self.age = age
        self.city = city

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def print_user_data(self):
        print(f'Name = {self.name}, Age = {self.age}, City = {self.city}')

    def jsonify(self):
        json_string = json.dumps(self.__dict__)
        return json_string


cli_user = UserData()
cli_user.print_user_data()

cli_user.set_name('Foo')
cli_user.print_user_data()

web_user = UserData('Foo', 30, 'New York')
json_string = web_user.jsonify()
print(f'Web User: {json_string}')

api_user = UserData(name = 'Bar', age = 20, city = 'Mumbai')
print(f'API User: {api_user.name}')
api_user.print_user_data()
json_string = api_user.jsonify()
print(f'API User: {json_string}')