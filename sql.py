import sqlite3

conn = sqlite3.connect('hagwarts.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   surname TEXT,
   gender TEXT,
   faculty TEXT);
""")
conn.commit()


def add(name, surname, gender, faculty):
    cur.execute("INSERT INTO students (name, surname, gender, faculty) VALUES (?,?,?,?);",
                (name, surname, gender, faculty))
    conn.commit()

