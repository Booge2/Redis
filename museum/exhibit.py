import json
from database import Database


class Exhibit:
    def __init__(self, exhibit_id, title, description, type):
        self.exhibit_id = exhibit_id
        self.title = title
        self.description = description
        self.type = type
        self.db = Database()

    def save(self):
        exhibit_data = {
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "related_people": []
        }
        self.db.set(f'exhibit:{self.exhibit_id}', json.dumps(exhibit_data))

    @staticmethod
    def get(exhibit_id):
        db = Database()
        exhibit_data = db.get(f'exhibit:{exhibit_id}')
        if exhibit_data:
            exhibit_data = json.loads(exhibit_data)
            return Exhibit(exhibit_id, exhibit_data['title'], exhibit_data['description'], exhibit_data['type'])
        return None

    @staticmethod
    def delete(exhibit_id):
        db = Database()
        db.delete(f'exhibit:{exhibit_id}')

    def update(self, title=None, description=None, type=None):
        exhibit_data = json.loads(self.db.get(f'exhibit:{self.exhibit_id}'))
        if title:
            exhibit_data['title'] = title
        if description:
            exhibit_data['description'] = description
        if type:
            exhibit_data['type'] = type
        self.db.set(f'exhibit:{self.exhibit_id}', json.dumps(exhibit_data))

    def add_related_person(self, person_id):
        exhibit_data = json.loads(self.db.get(f'exhibit:{self.exhibit_id}'))
        if person_id not in exhibit_data['related_people']:
            exhibit_data['related_people'].append(person_id)
            self.db.set(f'exhibit:{self.exhibit_id}', json.dumps(exhibit_data))

    def get_related_people(self):
        exhibit_data = json.loads(self.db.get(f'exhibit:{self.exhibit_id}'))
        return exhibit_data['related_people']

    @staticmethod
    def get_all_exhibits():
        db = Database()
        keys = db.keys('exhibit:*')
        exhibits = []
        for key in keys:
            exhibit_data = db.get(key)
            if exhibit_data:
                exhibit_data = json.loads(exhibit_data)
                exhibits.append(
                    Exhibit(key.decode('utf-8').split(':')[1], exhibit_data['title'], exhibit_data['description'],
                            exhibit_data['type']))
        return exhibits

    @staticmethod
    def get_by_type(type):
        db = Database()
        keys = db.keys('exhibit:*')
        exhibits = []
        for key in keys:
            exhibit_data = db.get(key)
            if exhibit_data:
                exhibit_data = json.loads(exhibit_data)
                if exhibit_data['type'] == type:
                    exhibits.append(
                        Exhibit(key.decode('utf-8').split(':')[1], exhibit_data['title'], exhibit_data['description'],
                                exhibit_data['type']))
        return exhibits
