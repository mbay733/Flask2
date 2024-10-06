from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app, db)
# Solution
# https://stackoverflow.com/questions/59455520/flask-sqlalchemy-marshmallow-error-on-relationship-one-to-many
ma = Marshmallow()
ma.init_app(app)


# DONE. Обязательно добавить импорт для обработчиков author, quote, user
from api.handlers import author
from api.handlers import quote
from api.handlers import user