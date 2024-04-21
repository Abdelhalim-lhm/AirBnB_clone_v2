#!/usr/bin/python3
""" importing FLask """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def dusplay_hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """ Display c + text """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Display python + text """
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    """ definition of the listening point and port """
    app.run(host="0.0.0.0", port=5000)
