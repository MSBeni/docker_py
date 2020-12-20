"""
    Module Description
   'Basic flask app' is a basic example of webserver
    which is a hello world function
    Please try the docker image to run this code with this commands:
    $ docker run -it --name myflask1 -p 5000:5000 -v ${PWD}:/app python:3.7 bash
    in the docker bash then, first install the flask:
    root@......:/# pip install flask:1.1.1
    root@......:/# cd app
    root@......:/# export FLASK_APP=Basic_Flask_App.py        # exporting to make them visible to flask command
    root@......:/# export FLASK_DEBUG=1
    root@......:/# flask run --host=0.0.0.0                   # There you go ...
    root@......:/# exit                                       # Ctrl + c then type exit to leave the container
"""

from flask import Flask, request
from flask import __version__ as fv
import sys

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    """
        Args: expecting no arguments
        Returns:
            str: greetings message
        Note:
            uses 'request' global variable from flask module to read HTTP REST query parameters.
            if query parameter with key 'name' has no value, than uses 'World' as default
    """
    name = request.args.get("name", "World")
    return "Hello, {}!".format(name)


@app.route('/version')
def version() -> str:
    """
        Args: expecting no arguments
        Returns:
            str: Flask Version

    """
    return "Flask Version is {}".format(fv)


@app.route('/sys')
def sys_version() -> str:
    """
        Args: expecting no arguments
        Returns:
            str: System Version

    """
    return f"System Version is {sys.version}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')