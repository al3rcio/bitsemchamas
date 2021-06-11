from flask import Flask, redirect, render_template, request
from jinja2 import Environment, PackageLoader, select_autoescape

# Configure application
app = Flask(__name__)

env = Environment(
    loader=PackageLoader("application.py"),
    autoescape=select_autoescape()
)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def indice():

    return render_template('index.html')
