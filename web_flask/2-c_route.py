#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
        return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
        return "HBNB"

@app.route("/c/<text>")
def cText(text):
        """display C followed by the value of the text variable"""
            text = (text.replace("_", " "))
            return f'C {text}'

if __name__ == '__main__':
                app.run(host="0.0.0.0", port=5000, debug=True)
