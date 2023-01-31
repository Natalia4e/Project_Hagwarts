from logg import logging
import excep
import sql


def menu():
    logging.info("Запуск приложения")
    type_num = input("Выберите вариант работы с базой\n"
                     "1 - Добавить данные студента\n"
                     "2 - Изменить данные студента\n"
                     "3 - Удалить данные студента\n"
                     "4 - Найти студента\n"
                     "5 - Показать всё\n"
                     "6 - Выход\n")
    match type_num:
        case "1":
            logging.info("Добавляем студента")
            print("Добавляем студента")
            a, b, c, d = excep.data_input()
            sql.add(a, b, c, d)
           
        case "2":
            logging.info("Изменяем данные")
            print("Изменяем данные")
            excep.change_student_data()
            
        case "3":
            logging.info("Удаление студента")
            excep.delete_student_data()

        case "4":
            logging.info("Поиск студента")
            excep.search_student_data()

        case "5":
            logging.info("Вывод всей БД")
            excep.show_all()

        case "6":
            logging.info("Выход")
            print("\n\nДо встречи!\n\n")
            
        case _:
            logging.error("Некорректный выбор режима")
            print("\n\nНекорректный выбор режима\n")
            menu()
