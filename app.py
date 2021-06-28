# linha pra criar o servidor
# export FLASK_APP=application.py

from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():

        return render_template('index.html')

@app.route("/hw")
def hw():

        return render_template('hw.html')

@app.route("/bec")
def bec():
        return render_template('bec.html')

@app.route("/eqt")
def eqt():

        return render_template('eqt.html')

@app.route("/feq")
def feq():

        return render_template('feq.html')

@app.route("/cave")
def cave():

        return render_template('cave.html')

@app.route("/2020")
def doismilevinte():

        return render_template('2020.html')

@app.route("/2050")
def doismilecinquenta():

        return render_template('2050.html')

@app.route("/thx")
def thx():

        return render_template('thx.html')

