#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that starts a Flask web application.
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """ closes or deallocates the resource if exists"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def all_cities():
    """ Displays a HTML page """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html',
                           states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
