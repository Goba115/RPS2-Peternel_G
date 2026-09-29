import sqlite3

# 1. Povezovanje z bazo podatkov
# Ustvari ali odpre datoteko 'lokalna.db'. Če datoteka še ne obstaja, jo Python samodejno ustvari.
conn = sqlite3.connect("lokalna.db")

# Ustvarimo kazalec (cursor), s pomočjo katerega izvajamo SQL ukaze in beremo podatke.
cursor = conn.cursor()

# 2. Ustvarjanje tabele
# Ukaz ustvari tabelo 'test', če ta še ne obstaja.
# Stolpec 'id' je primarni ključ, ki se samodejno povečuje ob vsakem novem zapisu.
# Stolpec 'besedilo' shranjuje tekstovne podatke.
cursor.execute("""
CREATE TABLE IF NOT EXISTS test 
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        besedilo TEXT
    )
""")

# 3. Vstavljanje podatkov
# V tabelo 'test' vstavimo novo vrstico z vrednostjo 'Deluje!'.
cursor.execute("INSERT INTO test (besedilo) VALUES ('Deluje!')")

# Shranimo (potrdimo) vse spremembe v bazi. Brez tega ukaza se podatki ne bi trajno shranili na disk.
conn.commit()

# 4. Branje in izpis podatkov
# Izberemo vse vrstice in vse stolpce iz tabele 'test'.
cursor.execute("SELECT * FROM test")

# Metoda fetchall() pridobi vse vrnjene vrstice in jih shrani v obliki seznama naborov (list of tuples).
rezultati = cursor.fetchall()

# Izpišemo rezultate v konzolo.
print("Vsebina tabele test:")
print(rezultati)

# 5. Zapiranje povezave
# Varno zapremo povezavo z bazo podatkov, da sprostimo sistemske vire.
conn.close()

# Prekinemo izvajanje skripte.
exit()
