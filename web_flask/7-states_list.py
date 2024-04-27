#!/usr/bin/python3
""" importing modules """
from flask import Flask, render_template
from models import *
from models import storage

from operator import attrgetter
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ states sorted list retriver """
    state_list = list(storage.all("State").values())
    states = sorted(state_list, key=attrgetter("name"))
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_app(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    """ definition of the listening point and port """
    app.run(host="0.0.0.0", port=5000)
