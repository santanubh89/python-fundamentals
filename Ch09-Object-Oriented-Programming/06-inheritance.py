class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f'login (parent): Logged in as {self.username}')

    def logout(self):
        print(f'logout (parent): Logging out user {self.username}')

    def fetch_data(self):
        print(f'fetch_data (parent): Username: {self.username} | Password: {self.password}')

class SystemUser(UserData):
    def __init__(self, username, password, role):
        super().__init__(username, password)
        self.role = role

    def login(self):
        print(f'login (SystemUser): {self.username} Logged in as {self.role}')

class EndUser(UserData):
    def logout(self):
        print(f'logout (Enduser) called in child class - will call parent')
        super().logout()

print(f'------Inspecting Child: SystemUser------')
sys_user = SystemUser('Foo', 'Secret', 'Admin')
sys_user.login()
sys_user.fetch_data()
sys_user.logout()

print(f'------Inspecting Child: EndUser------')
end_user = EndUser('Bar', 'Password')
end_user.login()
end_user.fetch_data()
end_user.logout()

print(f'------Inspecting Child: GeneralUser------')
general_user = UserData('Baz', None)
general_user.login()
general_user.fetch_data()
general_user.logout()