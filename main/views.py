from flask import render_template as render
from . import main


@main.route("/")
def index ():
    return render("index.html")