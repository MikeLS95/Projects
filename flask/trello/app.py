from marshmallow import ValidationError
from init import app
from blueprints.cli_bp import db_commands
from blueprints.cards_bp import cards_bp
from blueprints.users_bp import users_bp


app.register_blueprint(db_commands)
app.register_blueprint(cards_bp)
app.register_blueprint(users_bp)

    
@app.route('/')
def index():
    return 'Hello World!'


@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'ERROR': 'Not Found'}


@app.errorhandler(ValidationError)
def invalid_request(err):
    return {'ERROR': vars(err)["messages"]}, 400


@app.errorhandler(KeyError)
def missing_key(err):
    return {'ERROR': f"Missing field: {str(err)}"}, 400


print(app.url_map)