from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo


# DONE. Форма для регистрации
class RegistrationForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField(
        'Password', [InputRequired(), EqualTo('confirm', message="Passwords must match")]
    )
    confirm = PasswordField('Confirm password', [InputRequired()])


# DONE. Форма для логина
class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])