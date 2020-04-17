from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/you")
def you():
    return "Hello, you."

@app.route("/<string:name>")
def hello(name):
    return f"<h1>hello {name}<h1>"