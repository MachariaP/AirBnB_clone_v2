#!/usr/bin/env python3

" A script that starts a Flask web application"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """ Returns a string """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ Returns a string """
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    """ Returns a string """
    return 'C %s' % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
