import mysql.connector

def dbConnect():
    return mysql.connector.connect(
      host = "localhost",
      user = "baza",
      password = "baza",
      database = "aaa"
    )