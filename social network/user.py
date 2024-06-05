import json
from database import Database


class User:
    def __init__(self, username, password, full_name, email):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email
        self.db = Database()

    def save(self):
        user_data = {
            "password": self.password,
            "full_name": self.full_name,
            "email": self.email,
            "friends": [],
            "posts": []
        }
        self.db.set(self.username, json.dumps(user_data))

    @staticmethod
    def get(username):
        db = Database()
        user_data = db.get(username)
        if user_data:
            user_data = json.loads(user_data)
            return User(username, user_data['password'], user_data['full_name'], user_data['email'])
        return None

    @staticmethod
    def delete(username):
        db = Database()
        db.delete(username)

    @staticmethod
    def exists(username):
        db = Database()
        return db.exists(username)

    def update(self, full_name=None, email=None):
        user_data = json.loads(self.db.get(self.username))
        if full_name:
            user_data['full_name'] = full_name
        if email:
            user_data['email'] = email
        self.db.set(self.username, json.dumps(user_data))

    def add_friend(self, friend_username):
        user_data = json.loads(self.db.get(self.username))
        if friend_username not in user_data['friends']:
            user_data['friends'].append(friend_username)
            self.db.set(self.username, json.dumps(user_data))

    def get_friends(self):
        user_data = json.loads(self.db.get(self.username))
        return user_data['friends']

    def add_post(self, post_id):
        user_data = json.loads(self.db.get(self.username))
        user_data['posts'].append(post_id)
        self.db.set(self.username, json.dumps(user_data))

    def get_posts(self):
        user_data = json.loads(self.db.get(self.username))
        return user_data['posts']
