import sqlite3
import csv

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

a_file = open("poem.csv", encoding="utf8")
rows = csv.reader(a_file)
print(rows)
cur.executemany(
    "INSERT INTO poems_bengalipoems( title,poet,poem) VALUES (?, ?, ?)", rows)

con.commit()
con.close()
