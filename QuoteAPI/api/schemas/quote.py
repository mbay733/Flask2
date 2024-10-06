from api import ma
from marshmallow import EXCLUDE
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema


def rating_validate(value: int):
    # if return False -> raise ValidationError
    return value in range(1, 6)


class QuoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteModel
        unknown = EXCLUDE

    id = ma.auto_field()
    text = ma.auto_field()
    author = ma.Nested(AuthorSchema())
    rating = ma.Integer(strict=True, validate=rating_validate)


quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)
quote_without_rating = QuoteSchema(exclude=["rating"])