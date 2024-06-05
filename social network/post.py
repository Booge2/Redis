import json
from database import Database

class Post:
    def __init__(self, post_id, username, content):
        self.post_id = post_id
        self.username = username
        self.content = content
        self.db = Database()

    def save(self):
        post_data = {
            "username": self.username,
            "content": self.content
        }
        self.db.set(f'post:{self.post_id}', json.dumps(post_data))

    @staticmethod
    def get(post_id):
        db = Database()
        post_data = db.get(f'post:{post_id}')
        if post_data:
            post_data = json.loads(post_data)
            return Post(post_id, post_data['username'], post_data['content'])
        return None
