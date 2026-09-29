# LIBRARIES
from flask import Flask
from flask import render_template
from flask import request
import sqlite3


app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 8080
DATABASE_FILE = "lokalna.db"

# povezava na bazo
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

#test baze
def test_baze():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS test 
        (
            besedilo TEXT
        )
        """)
    cursor.execute("INSERT INTO test (besedilo) VALUES ('Deluje')")
    cursor.execute("SELECT * FROM test")
    rezultati = cursor.fetchall()
    print("odgovor baze: ")
    print(rezultati)
    cursor.execute("drop table test")
    conn.commit()
    conn.close()
    if rezultati:
        return True
    else:
        return False
# GLAVNI ROUTE APLIKACIJE

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    data = {
        "uspeh" : test_baze(),
        "itm" : None,
        "teza" : None,
        "visina" : None
    }
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