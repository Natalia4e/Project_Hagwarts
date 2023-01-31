import sqlite3
import logg
import ui

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
    logg. logging.info(
        f"Добавление студента {name} {surname} {gender} {faculty}")
    cur.execute("INSERT INTO students (name, surname, gender, faculty) VALUES (?,?,?,?);",
                (name, surname, gender, faculty))
    conn.commit()
    print(f"Студент {name} {surname} {gender} {faculty} успешно добавлен!\n\n\n")
    ui.menu()

