import logging

import excep


def menu():
    while True:
        type_num = input("Choise\n"
                         "1 - add_student\n"
                         "2 - change_data\n"
                         "3 - delete_student\n"
                         "4 - search_data\n"
                         "6 - show_all\n"
                         "5 - exit\n")
        match type_num:
            case "1":
                excep.add_student_data()
                pass
            case "2":
                excep.change_student_data()
                pass
            case "3":
                excep.delete_student_data()
                pass
            case "4":
                excep.search_student_data()
                pass
            case "5":
                logging.info("Stop program")
            case "6":
                excep.show_all()
            case _:
                logging.error("ERROR")
                print("ERR")


menu()
