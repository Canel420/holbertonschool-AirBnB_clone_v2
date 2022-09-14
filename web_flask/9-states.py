#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """ closes or deallocates the resource if exists"""
    storage.close()


@app.route('/states', strict_slashes=False)
def all_states():
    """ Display a HTML page with states """
    return render_template('7-states_list.html',
                           states=storage.all(State))


@app.route('/states/<string:id>', strict_slashes=False)
def search_state(id=None):
    """ Displays a Html page with a state search """
    return render_template('9-state.html',
                           states=storage.all(State)
                           .get('State.{}'.format(id)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
