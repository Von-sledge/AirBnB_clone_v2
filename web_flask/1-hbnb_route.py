#!/usr/bin/python3

"""A script that starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
"""

import flask as flask
app = flask.Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!' in the route '/'."""
    return "Hello HBNB!"

def hbnb():
    """Display 'HBNB' in the route '/hbnb'."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)