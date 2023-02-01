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

# students = [('4', 'Drako', 'Malfoi', 'm', 'Slytherin'), ('5', 'Vincent ', 'Crabbe', 'm', 'Slytherin'),
#           ('6', 'Terry', 'Boot', 'm', 'Ravenclaw'), ('7', 'Hannah', 'Longbottom', 'f', 'Hufflepuff'),
#            ('8', 'Padma', 'Patil', 'f', 'Gryffindorf'), ('9', 'Ronald', 'Weasley', 'm', 'Gryffindorf'),
#           ('10', 'Daphne', 'Greengrass', 'f', 'Slytherin'), ('11', 'Anthony', 'Goldstein', 'm', 'Ravenclaw')]

# cur.executemany("INSERT INTO students VALUES(?, ?, ?, ?, ?);", students)
# conn.commit()


def add(name, surname, gender, faculty):
    cur.execute("INSERT INTO students (name, surname, gender, faculty) VALUES (?,?,?,?);",
                (name, surname, gender, faculty))
    conn.commit()

