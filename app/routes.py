from flask import jsonify
from app import app
from app.models import db, Player


@app.route('/players')
def getPlayers():
    return jsonify({'Players': [p.to_dict() for p in Player.query.all()]}), 200