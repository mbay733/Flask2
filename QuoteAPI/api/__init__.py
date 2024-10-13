from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth

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
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    from api.models.user import UserModel
    user = db.one_or_404(db.select(UserModel).filter_by(username=username))
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True



# DONE. Обязательно добавить импорт для обработчиков author, quote, user
from api.handlers import author
from api.handlers import quote
from api.handlers import user