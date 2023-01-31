import sql

def input_integer(message, message_error): # не понял, как это работает. Должно проверять, есть ли такой id в БД? Или должен проверять, что введен корректный формат?
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


def add_student_data_check(name, sur_name, gender, faculty):
    # тут будет проверка корректности данных
    
    sql.add(name, sur_name, gender, faculty)


def show_all_check():
    # тут будет проверка, существует ли таблица. Нужна эта проверка или библиотека автоматически это делает?
    sql.cur.execute('SELECT * FROM students;')
    result = sql.cur.fetchall()
    print(result)


def change_student_data():
    id_for_changing = input_integer('Введите id студента, информацию о котором хотите именить в БД: ', 'Введите корректное id' )
    new_name = input("Введите новое имя студента: \n")
    new_sur_name = input("Введите Фамилию \n")
    new_gender = input("Введите пол \n")
    new_faculty = input("Введите факультет \n")

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
    delete_st = input_integer('Введите id студента, которого хотите удалить из БД: ', 'Введите корректное id')
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
