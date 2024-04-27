#!/usr/bin/python3
""" importing modules """
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ render states list """
    states = storage.all("State").values()
    return render_template(
            '9-states.html', states=states, cond="states_list")


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ render state ids """
    states_all = storage.all('State')
    try:
        state_id = states_all[id]
        return render_template(
                '9-states.html', state_id=state_id, cond="states_id")
    except Exception:
        return render_template('9-states.html', cond="not_found")


@app.teardown_appcontext
def teardown_app(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    """ definition of the listening point and port """
    app.run(host="0.0.0.0", port=5000)
