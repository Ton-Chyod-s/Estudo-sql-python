import sqlite3

conn = sqlite3.connect("myframecg.db")
cursor = conn.cursor()

print(cursor)