"""routes """
from flask import render_template
from taskmanager import app, db # noqa


@app.route("/")
def home():
    """ base """
    return render_template("base.html")
