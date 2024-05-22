#!/usr/bin/python
"""

"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@pp.teardown_appcontext
def teardown(exception):
    """

    """
    storagre.close()

@app.route('/states', strict_slashes=False)
def states_list():
    """

    """
    states = storage.all(State)
    return render_template('9-states_list.html', states=states)

@app.route('/states', defaults={"id": 1}, strict_slashes=False)
@app.route('/states/<div>', strict_slashes=False)
def states_by_id(id):
    """

    """
    if id == 1:
        states = storage.all(State)
        return render_template('9-states.html', states=states)
    else:
        for state in strorage.all(State).values():
            if state.id == id:
                return render_template('9-states.html', state=state)
        return render_template('9-states.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
