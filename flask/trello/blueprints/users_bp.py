from flask import Blueprint
# from auth import admin_only
from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token
from init import db, bcrypt
from models.user import User, UserSchema


users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/login', methods=['POST'])
def login():
    # Get the email and the password from the request
    params = UserSchema(only=['email', 'password']).load(
        request.json, unknown="exclude"
    )
    # email = request.json['email']
    # password = request.json['password']
    # [email, password] = request.json
    # Compare email and password against DB
    stmt = db.select(User).where(User.email == params['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']): 
        # Generate the JWT
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        # Return the JWT
        return {'token': token}
    else:
        # Error handling for wrong email/password (user not found)
        return {'ERROR' : 'Invalid email or password'}, 401