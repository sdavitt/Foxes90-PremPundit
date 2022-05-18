from app import app
from app.models import db, Player

# shell context processor - gives my flask shell (a little terminal that has access to my flask app) access to database models, etc.
@app.shell_context_processor
def shell_context():
    return {'db': db, 'Player': Player}