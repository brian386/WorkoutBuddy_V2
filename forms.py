from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, validators
from wtforms.validators import Length
from django.core.exceptions import ValidationError
from models import User

"""
Form Validators
"""

def username_isUnique(form, field):
    if User.query.get(field.id) is not None:
        raise ValidationError('Username must be unique')

def user_exists(form, field):
    if User.query.get(field.data) is None:
        raise ValidationError('User does not exist')

def login_success(form, field):
    if User.query.get(field.data).password != field.data:
        raise ValidationError(User.query.get(field.data).password+" "+field.data)

"""
Form Classes inherited from WTForms
"""

class LoginForm(FlaskForm):
    username = StringField('username', [user_exists])
    password = PasswordField('password', [login_success])

class RegisterForm(FlaskForm):
    id = StringField('username', [validators.Length(min=3, message="Your username should be at least 3 characters long."), username_isUnique])
    password = PasswordField('password', [validators.Length(min=6, message="Your password should be at least 6 characters long.")])
    email = StringField('email', [validators.Email(message="Your email should be in valid form.")])



