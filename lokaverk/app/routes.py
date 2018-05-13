from app import db
from app.models import User, Post, Myndir, Contact, Index
from flask_login import current_user, login_user, logout_user
from flask import render_template, redirect, flash, request
from app.forms import LoginForm, BlogForm, ContactForm
from app import app, photos

@app.route('/')
@app.route('/index')
def index():
    posts = Index.query.all()
    return render_template('index.html', posts=posts)

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
                flash('TLogin tókst')
                return redirect('/index')
            else:
                flash('Vitlaust notendanafn eða lykilorð')
                return redirect('/login')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/myndir', methods=['GET', 'POST'])
def upload():
    if current_user.is_authenticated:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            m = Myndir(link='../static/'+filename)
            db.session.add(m)
            db.session.commit()
            return redirect('/myndir')
    myndir = Myndir.query.all()
    return render_template('myndir.html', myndir=myndir)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        p = Contact(title=form.type.data, body=form.body.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/contact')
    contact = Contact.query.all()
    return render_template('contact.html', form=form, contact=contact)

@app.route('/updates', methods=['GET', 'POST'])
def updates():
    form = BlogForm()
    if form.validate_on_submit():
        p = Post(title=form.title.data, body=form.body.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/updates')
    posts = Post.query.all()
    return render_template('updates.html', form=form, posts=posts)

@app.route('/breyta/<page>/<no>', methods=['GET', 'POST'])
def breyta(page,no):
    if current_user.is_anonymous or int(no) < 0:
        return redirect('/index')
    post1 = Contact.query.get(no)
    form1 = ContactForm(obj=post1)
    if form1.validate_on_submit():
        db.session.delete(post1)
        db.session.commit()
        p = Contact(title=form1.type.data, body=form1.body.data)
        db.session.add(p)
        db.session.commit()
        return redirect('/contact')
    post2 = Post.query.get(no)
    form2 = BlogForm(obj=post2)
    if form2.validate_on_submit():
        db.session.delete(post2)
        db.session.commit()
        if post2.title[-8:] == '(Breytt)':
            p = Post(title=form2.title.data, body=form2.body.data, timestamp=post2.timestamp)
        else:
            p = Post(title=form2.title.data + ' (Breytt)', body=form2.body.data, timestamp=post2.timestamp)
        db.session.add(p)
        db.session.commit()
        return redirect('/updates')
    return render_template('breyta.html',page=page,no=no,form1=form1,form2=form2)

@app.route('/breyta2/<no>', methods=['GET', 'POST'])
def breyta2(no):
    if current_user.is_anonymous or int(no) < 0:
        return redirect('/index')
    post3 = Index.query.get(no)
    form3 = BlogForm(obj=post3)
    if form3.validate_on_submit():
        db.session.delete(post3)
        db.session.commit()
        p = Index(title=form3.title.data, body=form3.body.data)
        db.session.add(p)
        db.session.commit()
        return redirect('index')
    return render_template('breyta2.html',no=no,form=form3)

@app.route('/eyda/<page>/<no>')
def eyda(page,no):
    if current_user.is_anonymous or int(no) < 0:
        return redirect('/index')
    if page == 'updates':
        DeletePost = Post.query.get(no)
        db.session.delete(DeletePost)
        db.session.commit()
        return redirect('/updates')
    elif page == 'myndir':
        DeletePhoto = Myndir.query.get(no)
        db.session.delete(DeletePhoto)
        db.session.commit()
        return redirect('/myndir')
    elif page == 'contact':
        DeleteContact = Contact.query.get(no)
        db.session.delete(DeleteContact)
        db.session.commit()
        return redirect('/contact')
