import sqlite3

DATABASE_FILE = "../lokalna.db"

# 1. Povezovanje z bazo podatkov
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

# 2. Ustvarjanje tabele in vstavljanje podatkov
if False:
    #cursor.execute("DROP TABLE dnevnik;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dnevnik
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            datumCas DATETIME,
            visina FLOAT,
            teza FLOAT,
            itm FLOAT
        )
    """)
    
    # POPRAVEK: Namesto NOW() uporabimo CURRENT_TIMESTAMP
    #cursor.execute("""
    #   INSERT INTO dnevnik (datumCas, visina, teza, itm)
    #  VALUES (CURRENT_TIMESTAMP, 180, 90, 40);
    #""")

    # Shranimo spremembe v bazo
    conn.commit()
    

    # Izvedemo poizvedbo
    cursor.execute("SELECT * FROM dnevnik")

# cursor.execute("")
cursor.execute("DROP TABLE IF EXISTS `dnevnik`;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS `dnevnik` (
        `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
        `DatumCas` TEXT DEFAULT NULL,
        `visina` REAL DEFAULT NULL,
        `teza` REAL DEFAULT NULL,
        `itm` REAL DEFAULT NULL
    );
""")
# 4. Branje in izpis podatkov
rezultati = cursor.fetchall()

print("Vsebina tabele dnevnik:")
print(rezultati)

# 5. Zapiranje povezave
conn.close()
