from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date, timedelta
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, Boolean
from typing import Optional
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import ValidationError


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'Ministry of Silly Walks'

app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello"
)

db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


class Card(db.Model):
    __tablename__ = "cards"

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # title = db.Column(db.String(100))
    title: Mapped[str] = mapped_column(String(100))
    # description = db.Column(db.Text())
    description: Mapped[Optional[str]] = mapped_column(Text())
    # date_created = db.Column(db.Date())
    date_created: Mapped[date]


# Marshmallow schema (NOT a db schema!)
# Used by Marshmallow to serialize and/or validate our SQLAlchemy models
class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date_created')


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'password')

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [
        User(
            email='admin@spam.com', 
            password=bcrypt.generate_password_hash('123').decode('utf8'), 
            is_admin=True
        ),
        User(
            email='user@spam.com', 
            name='User', 
            password=bcrypt.generate_password_hash('123').decode('utf8')
        )
    ]

    cards = [
            Card(
                title='Start the project', 
                description='Stage 1 - Create ERD', 
                date_created=date.today()
            ),
            Card(
                title='ORM Queries', 
                description='Stage 2 - Implement CRUD', 
                date_created=date.today()
            ),
            Card(
                title='Marshmallow', 
                description='Stage 3 - Implement JSONify of models', 
                date_created=date.today(),
            ),
    ]

    db.session.add_all(users)
    db.session.add_all(cards)

    db.session.commit()
    print('Users and Cards added')


def admin_only(fn):
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id, User.is_admin)
        user = db.session.scalar(stmt)
        if user:
            return fn()
        else:
            return {'ERROR' : 'You are not an admin'}, 403

    return inner


@app.route('/cards')
@admin_only
def all_cards():
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True, only=['id', 'title']).dump(cards)


@app.route('/cards/<int:id>')
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)


@app.route('/users/login', methods=['POST'])
def login():
    # Get the email and the password from the request
    params = UserSchema(only=['email', 'password']).load(request.json)
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
    
    
@app.route('/')
def index():
    return 'Hello World!'


@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'ERROR': 'Not Found'}


@app.errorhandler(ValidationError)
def invalid_request(err):
    return {'ERROR': vars(err)}

@app.errorhandler(KeyError)
def missing_key(err):
    return {'ERROR': str(err)}