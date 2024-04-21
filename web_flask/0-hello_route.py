#!/usr/bin/python3
""" importing FLask """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    """ definition of the listening point and port """
    app.run(host="0.0.0.0", port=5000)
