class UserCredentialsModel:

    def __init__(self,email,username,password,hint):
        self.email = email
        self.username = username
        self.password = password
        self.hint = hint

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_hint(self, hint):
        self.hint = hint

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_hint(self):
        return self.hint

    def to_string(self):
        return f'Email: {self.email} | Username: {self.username} | Password: {self.password} | Hint: {self.hint}'
