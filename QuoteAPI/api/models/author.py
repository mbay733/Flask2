from api import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from api.models.quote import QuoteModel


class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), index=True, unique=True)
    # default -> for new instance, server_default -> for instances that already exist in table
    surname: Mapped[str] = mapped_column(String(32), index=True, default='Petrov', server_default="Smirnov")
    quotes: Mapped[list['QuoteModel']] = relationship(lambda: QuoteModel, back_populates='author', cascade="all, delete-orphan", lazy='dynamic')


    def __init__(self, name, surname='Petrov'):
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            }