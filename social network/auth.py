from user import User

class Auth:
    @staticmethod
    def login(username, password):
        user = User.get(username)
        if user and user.password == password:
            return True
        return False

    @staticmethod
    def register(username, password, full_name, email):
        if User.exists(username):
            return False
        user = User(username, password, full_name, email)
        user.save()
        return True
