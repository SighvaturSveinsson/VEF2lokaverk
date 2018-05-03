#Sighvatur Sveinsson


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if  u.set_password == u.check_password:
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/myndir')
def myndir():
    if logged in:
        v = true
        #ef v er true sýnir template option um að breyta
    return render_template('myndir.html', login=v)

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run()
