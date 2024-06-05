import json
from database import Database


class Person:
    def __init__(self, person_id, name, bio):
        self.person_id = person_id
        self.name = name
        self.bio = bio
        self.db = Database()

    def save(self):
        person_data = {
            "name": self.name,
            "bio": self.bio,
            "related_exhibits": []
        }
        self.db.set(f'person:{self.person_id}', json.dumps(person_data))

    @staticmethod
    def get(person_id):
        db = Database()
        person_data = db.get(f'person:{person_id}')
        if person_data:
            person_data = json.loads(person_data)
            return Person(person_id, person_data['name'], person_data['bio'])
        return None

    @staticmethod
    def delete(person_id):
        db = Database()
        db.delete(f'person:{person_id}')

    def update(self, name=None, bio=None):
        person_data = json.loads(self.db.get(f'person:{self.person_id}'))
        if name:
            person_data['name'] = name
        if bio:
            person_data['bio'] = bio
        self.db.set(f'person:{self.person_id}', json.dumps(person_data))

    def add_related_exhibit(self, exhibit_id):
        person_data = json.loads(self.db.get(f'person:{self.person_id}'))
        if exhibit_id not in person_data['related_exhibits']:
            person_data['related_exhibits'].append(exhibit_id)
            self.db.set(f'person:{self.person_id}', json.dumps(person_data))

    def get_related_exhibits(self):
        person_data = json.loads(self.db.get(f'person:{self.person_id}'))
        return person_data['related_exhibits']
