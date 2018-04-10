#Sighvatur Sveinsson
#Nota plugins: Flask, Alchemy?, mysqlLite?

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/myndir')
def myndir():
    return render_template('myndir.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run()
