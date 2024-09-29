from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

class Base(DeclarativeBase):
    pass



app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app, db)

# TODO. Обязательно добавить импорт для обработчиков author и quote