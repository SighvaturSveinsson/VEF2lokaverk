from app.models import User
from flask_login import current_user, login_user, logout_user
from flask import Flask, render_template, redirect, flash
from app.forms import LoginForm, BlogForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        users = User.query.all()
        user = User.query.filter_by(username=form.username.data).first()
        for u in users:
            if form.username.data == u.username and form.password.data == u.password:
                login_user(user, remember=form.remember_me.data)
                flash('Login tókst')
                return redirect('/index')
            else:
                flash('Invalid username or password')
                return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

''''
@app.route('/myndir')
def myndir():
    return render_template('myndir.html')
'''


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/updates', methods=['GET', 'POST'])
def updates():
    form = BlogForm()
    posts = Post.query.all()
    return render_template('contact.html', form=form, posts=posts())
