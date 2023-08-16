from bottle import route, run, template
import numpy as np


@route("/hello/<name>")
def index(name):
    return template("<b>Hello {{name}}</b>!", name=name)


@route("/get_numbers")
def get_numbers():
    arr = np.random.rand(3, 2)
    return template("{{arr}}", arr=arr)


run(host="localhost", port=8080)
