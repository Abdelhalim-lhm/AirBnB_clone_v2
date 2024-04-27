#!/usr/bin/python3
""" importing FLask """
from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def isnumber(n):
    """ Display n is a number if n is an integer """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            iseven = 'even'
        else:
            iseven = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, iseven=iseven)


if __name__ == "__main__":
    """ definition of the listening point and port """
    app.run(host="0.0.0.0", port=5000)