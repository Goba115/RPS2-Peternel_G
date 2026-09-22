import sqlite3

conn = sqlite3.connect("lokalna.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, besedilo TEXT)"
)
cursor.execute("INSERT INTO test (besedilo) VALUES ('Deluje!')")
conn.commit()

# Preverimo izpis
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())

conn.close()
exit()
