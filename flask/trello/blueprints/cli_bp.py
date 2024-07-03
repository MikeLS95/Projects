from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.card import Card


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    users = [
        User(
            email='admin@spam.com', 
            password=bcrypt.generate_password_hash('123456').decode('utf8'), 
            is_admin=True
        ),
        User(
            email='user@spam.com', 
            name='User', 
            password=bcrypt.generate_password_hash('123456').decode('utf8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    cards = [
            Card(
                title='Start the project', 
                description='Stage 1 - Create ERD', 
                date_created=date.today(),
                user=users[0]
            ),
            Card(
                title='ORM Queries', 
                description='Stage 2 - Implement CRUD', 
                date_created=date.today(),
                user=users[1]
            ),
            Card(
                title='Marshmallow', 
                description='Stage 3 - Implement JSONify of models', 
                date_created=date.today(),
                user=users[0]
            ),
    ]

    db.session.add_all(cards)
    db.session.commit()

    print('Users and Cards added')