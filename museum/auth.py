import json
from database import Database

class Auth:
    def __init__(self):
        self.db = Database()

    def register(self, username, password):
        if self.db.exists(f'user:{username}'):
            return False
        user_data = {
            "password": password
        }
        self.db.set(f'user:{username}', json.dumps(user_data))
        return True

    def login(self, username, password):
        user_data = self.db.get(f'user:{username}')
        if user_data:
            user_data = json.loads(user_data)
            if user_data['password'] == password:
                return True
        return False
