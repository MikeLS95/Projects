from flask import Blueprint
from flask_jwt_extended import jwt_required
from auth import admin_only
from init import db
from models.card import Card, CardSchema


cards_bp = Blueprint('cards', __name__, url_prefix='/cards')


@cards_bp.route('/')
@admin_only
def all_cards():
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True, only=['id', 'title']).dump(cards)


@cards_bp.route('/<int:id>')
# @jwt_required()
def one_card(id):
    card = db.get_or_404(Card, id)
    return CardSchema().dump(card)