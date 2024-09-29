from api import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(32), index= True, unique=True)
    quotes: Mapped[list['QuoteModel']] = relationship(back_populates='author', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
            }