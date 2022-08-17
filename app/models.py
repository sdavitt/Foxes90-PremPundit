from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.String(250), primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    position = db.Column(db.String(20))
    team = db.Column(db.String(50))
    injured = db.Column(db.Boolean)
    suspended = db.Column(db.Boolean)

    def __init__(self, a_dict):
        self.id = str(uuid4())
        self.first_name = a_dict['first_name']
        self.last_name = a_dict['last_name']
        self.team = a_dict['team']
        self.position = a_dict['pos']
        if a_dict.get('injured'): # if there is an injured key in the dict
            self.injured = a_dict['injured']
        else:
            self.injured = False
        if a_dict.get('suspended'): # if there is an suspended key in the dict
            self.suspended = a_dict['suspended']
        else:
            self.suspended = False


    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'team': self.team,
            'position': self.position,
            'injured': self.injured,
            'suspended': self.suspended
        }


# class Team(db.Model):
#     """
#     Add complexity to the project by introducing specifics of how each team operates
#     """