from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Post')

class ContactForm(FlaskForm):
    type = SelectField('Type', choices=[('Símanúmer:','Símanúmer'),('Tölvupóstur:','Tölvupóstur'),('Facebook:','Facebook')], validators=[DataRequired()])
    body = StringField('Info', validators=[DataRequired()])
    submit = SubmitField('Post')