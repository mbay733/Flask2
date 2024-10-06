from api import db
from sqlalchemy.orm import Mapped, mapped_column, relationship, WriteOnlyMapped
from sqlalchemy import String


class AuthorModel(db.Model):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(32), index=True, unique=True)
    # default -> for new instance, server_default -> for instances that already exist in table
    surname: Mapped[str] = mapped_column(String(32), index=True, default='Petrov', server_default="Smirnov")
    quotes: Mapped[list['QuoteModel']] = relationship(back_populates='author', cascade="all, delete-orphan", lazy='dynamic')


    def __init__(self, name, surname='Petrov'):
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            }