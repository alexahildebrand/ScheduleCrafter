from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Choose your classes<h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username} </h1>'

@app.route('/options/<major>')
def class_options(major):
    return f'<h1> These are the class options for {major} </h1>'
