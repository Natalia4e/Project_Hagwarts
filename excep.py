import re
import sql
import logg
import ui


def check_id(x):
    sql.cur.execute("SELECT id FROM students;")
    available_ids = [i[0] for i in sql.cur.fetchall()]
    return x in available_ids


def check_in_data(data, op, meta):
    pruve = None
    while True:
        if op == 1 and (not re.match(r"^[A-Za-zа-яА-ЯёЁ ]*$", data) is None):
            pruve = True
        elif op == 2 and (data == 'f' or data == 'm'):
            pruve = True
        elif op == 3 and (data == 'Hufflepuff' or data == 'Ravenclaw' or data == 'Gryffindorf' or data == 'Slytherin'):
            pruve = True
        if pruve:
            return data
        else:
            print(f"Убедитесь, что ввели корректные данные: {meta}\n")
            data = input("Еще раз\n")
            logg.logging.error(f"Ошибка при вводе параметра {meta}")
            continue


def data_input():
    name = check_in_data(input("Имя:\n"), 1, "Имя")
    sur_name = check_in_data(input("Фамилия:\n"), 1, "Фамилия")
    gender = check_in_data(input("Пол: женский - f; мужской - m\n"), 2, "Пол")
    faculty = check_in_data(input(
        "Факультет: Hufflepuff, Ravenclaw, Gryffindorf или Slytherin\n"), 3, "Факультет")
    return name, sur_name, gender, faculty


def data_input_new_student():
    name = check_in_data(input("Новое имя:\n"), 1, "Имя")
    sur_name = check_in_data(input("Новая фамилия:\n"), 1, "Фамилия")
    gender = check_in_data(
        input("Новый пол: женский - f; мужской - m\n"), 2, "Пол")
    faculty = check_in_data(input(
        "Новый факультет: Hufflepuff, Ravenclaw, Gryffindorf или Slytherin\n"), 3, "Факультет")
    return name, sur_name, gender, faculty


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


def show_all():
    # тут будет проверка, существует ли таблица. Нужна эта проверка или библиотека автоматически это делает?
    sql.cur.execute('SELECT * FROM students;')
    result = sql.cur.fetchall()
    for i in result:
        print(*i)
    print('\n\n')
    ui.menu()


def change_student_data():
    id_for_changing = input_integer(
        'Введите id студента, информацию о котором хотите именить в БД: ', 'Введите корректное id')
    new_name, new_sur_name, new_gender, new_faculty = data_input_new_student()

    names = []
    inputs = []
    query = "UPDATE students SET "

    if new_name != '':
        names.append('name')
        inputs.append(new_name)

    if new_sur_name != '':
        names.append('surname')
        inputs.append(new_sur_name)

    if new_gender != '':
        names.append('gender')
        inputs.append(new_gender)

    if new_faculty != '':
        names.append('faculty')
        inputs.append(new_faculty)

    inputs.append(id_for_changing)

    query += " = ?,".join(names) + ' = ?' + " WHERE id = ?;"
    sql.cur.execute(query, tuple(inputs))
#
    print(query)


# удаляем всю строку
def delete_student_data():
    # Нужна проверка, существует ли такой id
    delete_st = input_integer(
        'Введите id студента, которого хотите удалить из БД: ', 'Введите корректное id')
    if check_id(delete_st):
        sql.cur.execute("DELETE FROM students WHERE id = ?;",
                        (str(delete_st)))
        sql.conn.commit()
        # result = sql.cur.fetchall()
        print(f"Студент с id {delete_st} успешно удален")
        ui.menu()
    else:
        delete_student_data()


def search_student_data():
    search = input(
        "Введите искомое значение: имя, фамилию или факультет или 00 для отмены\n")
    # Нужна проверка данных
    if search == '00':
        print('Отмена')
    else:
        logg.logging.info(f"Поиск студента {search}")
        sql.cur.execute('SELECT * FROM students WHERE name LIKE ? OR surname LIKE ? OR faculty LIKE ?;',
                        (('%'+search+'%'), ('%'+search+'%'), ('%'+search+'%')))
        result = sql.cur.fetchall()
        if result == []:
            search_student_data()
        print(result)

    print()
