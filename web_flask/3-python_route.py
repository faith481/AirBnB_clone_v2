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

def c_page(text):
    """display C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python/<text>")
@app.route("/python", defaults={"text": "is cool"})
def python_page(text):
    """The Python page displayed by the value of <text>"""
    text = text.replace("_", " ")
    return f"Python {text}"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
