from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello'

db = SQLAlchemy(app)

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    date_created = db.Column(db.Date())


@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    cards = [
            Card(title='Start the project', description='Stage 1 - Create ERD', date_created=date.today()),
            Card(title='ORM Queries', description='Stage 2 - Implement CRUD', date_created=date.today()),
            Card(title='Marshmallow', description='Stage 3 - Implement JSONify of models', date_created=date.today())
    ]

    db.session.add_all(cards)

    db.session.commit()


@app.cli.command('all_cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card).where(Card.id < 3)
    cards = db.session.scalars(stmt)
    for card in cards:    
        print(card)




@app.route('/')
def index():
    return 'Hello World!'

