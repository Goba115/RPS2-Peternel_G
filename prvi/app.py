# LIBRARIES
from flask import Flask
from flask import render_template
from flask import request
import sqlite3


# MY LIBRARIES
from modules import dbLogic

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 8080

# GLAVNI ROUTE APLIKACIJE

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    data = {
        "uspeh" : False,
        "itm" : None,
        "teza" : None,
        "visina" : None
    }
    data["uspeh"] = dbLogic.getAll()
    if request.method == "POST":
            data["teza"] = request.form.get("teza")
            data["visina"] = request.form.get("visina")
            if data["visina"] and data["teza"]: 
                data["itm"] = izracun_itm(float(data["teza"]) , float(data["visina"]))
            print(data)
    
    return render_template("index.html", podatki = data)

def izracun_itm(teza_fun, visina_fun):
    return teza_fun + visina_fun

    


# ZAGON APLIKACIJE
app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)