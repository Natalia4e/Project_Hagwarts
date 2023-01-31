import sql


# проверка, что это число
def input_integer(message, message_error):
    a = None
    while True:
        if a is None:
            try:
                a = int(input(message))
                break
            except ValueError:
                print(message_error)
                continue

    return a

# проверка для пола
def input_gender(message, message_error):
    action = None
    while True:
        if action is None:
            val = input(message)
            if val in ['m', 'f']:
                action = val
                break
            else:
                print(message_error)
    return action


# проверка для факультета
def input_faculty(message, message_error):
    action = None
    while True:
        if action is None:
            val = input(message)
            if val in ['Griffindorf', 'Slytherin','Ravenclaw', 'Hufflepuff']:
                action = val
                break
            else:
                print(message_error)
    return action


def add_student_data():
    name = input("Введите имя \n")
    sur_name = input("Введите Фамилию \n")
    gender = input("Введите пол \n")

    faculty = input_faculty('Введите факультет: ', 'Введите корректный факультет: ')
    sql.add(name, sur_name, gender, faculty)


def show_all():
    sql.cur.execute('SELECT * FROM students;')
    result = sql.cur.fetchall()
    print(result)


def change_student_data():
    id_for_changing = input_integer('Введите id студента, информацию о котором хотите изменить в БД: ', 'Введите корректное id!')
    new_name = input("Введите новое имя студента: \n")
    new_sur_name = input("Введите Фамилию \n")
    new_gender = input_gender('Введите пол ', 'Введите корректный пол!')
    new_faculty = input_faculty('Введите факультет: ', 'Введите корректный факультет: ')

    names = []
    inputs = []
    query = "UPDATE students SET "

    if new_name != '':
        names.append('name')
        inputs.append( new_name )

    if new_sur_name != '':
        names.append('surname')
        inputs.append( new_sur_name )

    if new_gender != '':
        names.append('gender')
        inputs.append( new_gender )

    if new_faculty != '':
        names.append('faculty')
        inputs.append( new_faculty )

    inputs.append(id_for_changing)

    query += " = ?,".join(names) + ' = ?' + " WHERE id = ?;"
    sql.cur.execute(query, tuple(inputs))

    print(query)


#удаляем всю строку
def delete_student_data():
    delete_st = input_integer('Введите id студента, которого хотите удалить в БД: ', 'Введите корректное id!')
    sql.cur.execute('DELETE FROM students WHERE id = ?;',
                    ((delete_st)))
    result = sql.cur.fetchall()
    print(result)



def search_student_data():
    search = input("Введите искомое значение: \n")
    sql.cur.execute('SELECT * FROM students WHERE name LIKE ? OR surname LIKE ? OR faculty LIKE ?;',
                    (('%'+search+'%'), ('%'+search+'%'), ('%'+search+'%')))
    result = sql.cur.fetchall()
    print(result)

    print()
