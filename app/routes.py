from flask import jsonify, request
from app import app
from app.models import db, Player


@app.route('/players')
def getPlayers():
    """ [GET] all player information """
    return jsonify({'Players': [p.to_dict() for p in Player.query.all()]}), 200

# purpose of our POST request - to allow a user/dev/some code source to send us player data
# we need to specify how this data is organized/what data we are getting
# my POST request will accept a dictionary containing
    # REQUIRED - all information that is non-nullable about my object
    # OPTIONAL - all optional attributes of my object
@app.route('/newplayer', methods=['POST'])
def createPlayer():
    """
    [POST] Create a new player in my database
    Accepts JSON data in the following format:
    {
        first_name: <STRING>,
        last_name: <STRING>,
        team: <STRING>,
        pos: <STRING> Midfielder | Defender | Keeper | Striker,
        injured: <OPTIONAL BOOLEAN>,
        suspended: <OPTIONAL BOOLEAN>
    }
    """
    try:
        # we need to access the payload/data from the request
        player_dict = request.get_json() # Python dictionary
        # then we need to transform it into a Player object
        new_player = Player(player_dict)
    except Exception as err:
        return jsonify({'Improper JSON data received': 'must follow the below format',
            'Proper Data Format': {
        'first_name': '<STRING>',
        'last_name': '<STRING>',
        'team': '<STRING>',
        'pos': '<STRING> Midfielder | Defender | Keeper | Striker',
        'injured': '<OPTIONAL BOOLEAN>',
        'suspended': '<OPTIONAL BOOLEAN>'
    }}), 406
    try:
        # then we need to upload it to our database
        db.session.add(new_player)
        db.session.commit()
        return jsonify({'Created': new_player.to_dict()}), 201
    # if there is a problem, send an error message
    except:
        return jsonify({'Create Player Rejected': 'A Player with that name already exists'}), 400