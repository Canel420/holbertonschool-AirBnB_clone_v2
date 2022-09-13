#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that starts a Flask web application.
"""
from email.policy import default
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
    """ Returns C letter plus given string """
    return 'C ' + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text='is cool'):
    """ Returns python plus given string"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """ Displays if given n is a number """
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
