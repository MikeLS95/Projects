from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text
from typing import Optional
from flask_marshmallow import Marshmallow


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello"
)


db = SQLAlchemy(model_class=Base)
db.init_app(app)
ma = Marshmallow(app)


class Card(db.Model):
    __tablename__ = 'cards'

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


@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

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

    db.session.add_all(cards)

    db.session.commit()


@app.route('/cards')
def all_cards():
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards)


@app.route('/cards/<int:id>')
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)


@app.route('/')
def index():
    return 'Hello World!'

@app.errorhandler(404)
def not_found(err):
    return {'ERROR': 'Not Found'}