from typing import Optional
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey
from marshmallow import fields
from marshmallow.validate import Regexp, And, Length
from init import db, ma


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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates='cards')


# Marshmallow schema (NOT a db schema!)
# Used by Marshmallow to serialize and/or validate our SQLAlchemy models
class CardSchema(ma.Schema):
    # Allow title to only have digits, letters or spaces
    title = fields.String(required=True, validate=And(
        Regexp('^[0-9a-zA-Z ]+$', error="Title must contain digits, letters or spaces only."),
        Length(min=5, error="Title must be at least 5 characters")
    ))
    user = fields.Nested('UserSchema', exclude=['password'])

    class Meta:
        fields = ('id', 'title', 'description', 'date_created', 'user')