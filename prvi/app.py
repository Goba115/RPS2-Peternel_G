from flask import Flask, render_template, request
import sqlite3
from datetime import datetime  # Dodano za avtomatski vpis časa

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 8080
DATABASE_FILE = "lokalna.db"

def test_baze():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (besedilo TEXT)")
    cursor.execute("INSERT INTO test (besedilo) VALUES ('Deluje')")
    cursor.execute("SELECT * FROM test")
    rezultati = cursor.fetchall()
    cursor.execute("DROP TABLE test")
    conn.commit()
    conn.close()
    return True if rezultati else False

def vsebina_baze():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `dnevnik` (
            `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
            `DatumCas` TEXT DEFAULT NULL,
            `visina` REAL DEFAULT NULL,
            `teza` REAL DEFAULT NULL,
            `itm` REAL DEFAULT NULL
        );
    """)
    cursor.execute("SELECT * FROM dnevnik;")
    podatki = cursor.fetchall()
    conn.close()
    return podatki

def shrani_v_bazo(visina, teza, itm):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    trenutni_cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO dnevnik (DatumCas, visina, teza, itm) 
        VALUES (?, ?, ?, ?)
    """, (trenutni_cas, visina, teza, itm))
    conn.commit()
    conn.close()

def izracun_itm(teza_fun, visina_fun):
    # Popravljena formula: teža / (višina_v_metrih ^ 2)
    # Če vpisuješ višino v cm (npr. 180), jo delimo s 100
    visina_m = visina_fun / 100 if visina_fun > 3 else visina_fun
    return round(teza_fun / (visina_m ** 2), 2)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    data = {
        "uspeh": test_baze(),
        "itm": None,
        "teza": None,
        "visina": None
    }
    if request.method == "POST":
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        if data["visina"] and data["teza"]: 
            data["itm"] = izracun_itm(float(data["teza"]), float(data["visina"]))
            # Shranimo izračun v bazo podatkov
            shrani_v_bazo(float(data["visina"]), float(data["teza"]), data["itm"])
    
    return render_template("index.html", podatki=data)

@app.route("/dnevnik", methods=["GET"])
def stran_dnev():
    data = {
        "vrednosti": vsebina_baze()  # Podatke naložimo takoj ob GET zahtevi
    }
    return render_template("dnevnik.html", podatki=data)

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(host=APP_ADDRESS, port=APP_PORT)
