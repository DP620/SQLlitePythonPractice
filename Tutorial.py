# import sql and the tutorial database
import sqlite3 as sq
import os

filename = "tutorial.db"
cleanFileName = filename.removesuffix(".db")
if os.path.exists(filename):
    os.remove(filename)
    print(f"removed {cleanFileName} file")
con = sq.connect(filename)


# creating cursor to fetch results from SQL queries
cur = con.cursor()

# create database table 'movie' with the columns 'title', 'year, 'score
# use column names in table decleration thanks to flexible typing
# specifying the data types is optional
# execute the 'CREATE TABLE' by calling cur.execute()
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)

cur.execute("""
    INSERT INTO movie VALUES
    ('WildWood', 2026, 9.2),
    ('Baby Driver', 2017, 10.0)
""")

con.commit()

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())

data = [
    ("Phantom Of The Paradise", 1974, 9.2),
    ("Spider-Man: Brand New Day", 2026, 9.8),
    ("Resident Evil", 2026, 8.3),
]

cur.executemany("INSERT INTO movie VALUES( ?, ?, ?)", data)
con.commit()
for row in cur.execute("SELECT year, title FROM movie ORDER BY score DESC"):
    print(row)
