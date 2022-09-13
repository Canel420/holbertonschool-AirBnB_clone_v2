#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB in specific route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_lang(text):
    """ Return C letter plus given string """
    return 'C ' + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
