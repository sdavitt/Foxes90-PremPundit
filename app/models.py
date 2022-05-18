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

    def __init__(self, fname, lname, team='Manchester City', pos='Midfield', inj=False, sus=False):
        self.id = uuid4()
        self.first_name = fname
        self.last_name = lname
        self.team = team
        self.position = pos
        self.injured = inj
        self.suspended = sus


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