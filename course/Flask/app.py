from flask import Flask  # first WSGI

app = Flask(__name__)  # for single module #output: <Flask "app">


# app = Flask("Flask")  # for myltiple module #output: <Flask "Flask">
@app.route("/")
def hello_world():
    return "Hello,World!"
