from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from init import db, ma


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'password', 'is_admin')
