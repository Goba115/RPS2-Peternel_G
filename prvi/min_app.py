# LIBRARIES
from flask import Flask
from flask import render_template
from flask import request
import sqlite3


app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 80

@app.route("/", methods = ["GET", "POST"])
    return render_template("index.html", podatki = data)




# ZAGON APLIKACIJE
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)