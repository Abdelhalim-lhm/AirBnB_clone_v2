#!/usr/bin/python3
""" importing modules """
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ render index6 like HTML """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template(
            '10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_app(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    """ definition of the listening point and port """
    app.run(host="0.0.0.0", port=5000)
