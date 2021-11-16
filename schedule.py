from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/schedule')
def schedule_page():
    items = Item.query.all()
    return render_template('schedule.html', items=items)

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username} </h1>'

@app.route('/options/<major>')
def class_options(major):
    return f'<h1> These are the class options for {major} </h1>'
