from api import db, app
from api.models.quote import QuoteModel
from api.models.author import AuthorModel
from typing import Any
from flask import jsonify, abort, request
from . import validate


# URL: /quotes
@app.route("/quotes")
def get_quotes() -> list[dict[str, Any]]:
    """ Функция неявно преобразовывает список словарей в JSON."""
    quotes_db = db.session.scalars(db.select(QuoteModel)).all()
    quotes = []
    for quote in quotes_db:
        quotes.append(quote.to_dict())
    return jsonify(quotes), 200


# URL: /authors/1/quotes
@app.route("/authors/<int:author_id>/quotes")
def get_author_quotes(author_id):
    """ Функция неявно преобразовывает список словарей в JSON."""
    author = db.session.get(AuthorModel, author_id)
    quotes = []
    for quote in author.quotes:
        quotes.append(quote.to_dict())
    
    return jsonify(author=author.to_dict() | {"quotes": quotes}), 200