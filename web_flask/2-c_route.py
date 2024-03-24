#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_page(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>")
@app.route("/python", defaults={"text": "is cool"})
def python_page(text):
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
