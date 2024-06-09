from typing import Optional
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
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


# Marshmallow schema (NOT a db schema!)
# Used by Marshmallow to serialize and/or validate our SQLAlchemy models
class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date_created')