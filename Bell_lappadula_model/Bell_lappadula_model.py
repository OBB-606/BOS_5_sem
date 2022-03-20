"""
Модель Белла - Лаппадулы - каноничный пример модели с мандатным разграничением доступа.
Есть метка конфиденциальности у объектов и субъектов.
У объектов - 1, 2, 3. Что соответсвует "С", "СС", "ОВ"
У субъектов - 1, 2, 3. Что соответсвует "guest", "user", "root"
Реализована политика "no write down" и "no read up".
"""

import csv
import json
import os
import sys

users_dict: dict = {}  # Словарь с информацией субъектов

def help():
    print("command's : "
          "check_rights - посмотреть права пользователя на файл\n"
          "remove_file - удалить файл\n"
          "read_file - прочитать файл\n"
          "write_file - вписать в файл\n"
          "clear_file - удалить содержимое файла\n"
          "logout_user - логаут\n"
          "refactor_type_object - поменять метку конфиденциальности у объекта\n"
          "create_object - создать объект\n"
          "create_user - создать субъекта\n"
          "login_user - зайти в систему под другим пользователем\n"
          "print_lists - вывести список существующих пользователей системы\n"
          "")


def save_users_file():
    with open("users.json", 'w') as json_file:
        json.dump(users_dict, json_file, indent=2)


def remove_file(filename: str, user: str):
    if users_dict["users"][user] >= users_dict["objects"][filename]:  # Если у субъекта мандат больше или
        # равен мандату объекта, то он может его удалить
        try:
            os.remove(filename)
        except IOError:
            print("Файл отсутствует!")
    else:
        print("You are not authorized for this action!")
        executor()


def clear_file(filename: str, user: str):
    if users_dict["users"][user] >= users_dict["objects"][filename]:  # Если у субъекта мандат больше или
        # равен мандату объекта, то он может его очистить от содержимого
        try:
            with open(filename, "w") as c_f:
                pass
        except IOError:
            print("IO Error!")
    else:
        print("You are not authorized for this action!")
        executor()


def write_file(filename: str, message: str, user: str):
    if users_dict["users"][user] <= users_dict["objects"][filename]:  # Если у субъекта мандат ниже или равен
        # мандату объекта, то он может в него писать, иначе - нет, т.е NWD - no write down
        try:
            handle = open(filename, 'a')
            handle.writelines(message)
        except IOError:
            print("IO Error!")
        finally:
            handle.close()
    else:
        print("You are not authorized for this action! (NWD)")
        executor()


def refactor_type_object(filename: str, user: str):  # Если у субъекта мандат выше чем у объекта, то он не может
    # записать в него ничего, поэтому ему надо поднимать мандат у объекта
    if users_dict["users"][user] > users_dict["objects"][filename]:
        new_type_this_object = int(input("write new type this object: "))
        users_dict["objects"][filename] = new_type_this_object
        save_users_file()
    else:
        print("You are not authorized for this action!")
        executor()


def read_file(filename: str, user: str):
    if users_dict["users"][user] >= users_dict["objects"][filename]:  # Если мандат субъекта больше или равен
        # мандату объекта, то он может его читать, а если нет, то нет) т.е NRU - no read up
        try:
            handle = open(filename, "r")
            print(handle.read())
        except IOError:
            print("File is not found!")
        finally:
            handle.close()
    else:
        print("You are not authorized for this action! (NRU)")
        executor()


def logout_user():
    sys.exit()


def create_object(filename: str, type_object: int):
    handle = open(filename, "w")
    handle.write("")
    handle.close()
    users_dict["objects"][filename] = type_object
    save_users_file()


def get_data_from_users_json():
    global users_dict
    try:
        with open('users.json', 'r') as json_file:
            users_dict = json.load(json_file)
    except:
        print("Error, file is empty")


login_list = []
password_list = []
login_password_list = []
login_list.append("root")
password_list.append("1234")

with open("login_password.csv", 'r') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        login_password_list.append(row)

for i in range(len(login_password_list)):
    login_list.append(login_password_list[i][0])
    password_list.append(login_password_list[i][1])

login = ""
password = ""

check = True


def print_lists():
    global login_list, password_list
    print(login_list)
    print(password_list)


def login_user():
    global login, password
    login = str(input("Write login:"))
    password = str(input("Write password:"))
    if login not in login_list and password not in password_list:
        print("Login or password is wrong!")
        login_user()


login_user()

while check:
    if login not in login_list or password not in password_list:
        print("login or password is wrong!")
        login_user()
    else:
        check = False
        break


def create_user():
    global login_list, password_list, login, password
    if login == "root" and password == "1234":
        login_new_user = str(input("login new user: "))
        password_new_user = str(input("password new user: "))
        if login_new_user not in login_list:
            tmp = [login_new_user, password_new_user]
            with open("login_password.csv", 'a', newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(tmp)
            type_user = int(input("write type user: "))
            users_dict["users"][login_new_user] = type_user
            save_users_file()
        else:
            print("this user is already exists")
    else:
        print("You are not authorized to do this.")
        executor()


if login == "exit":
    sys.exit()


def command_executor(command: str):
    if command == "create_object":
        name_object = str(input("write name object (with .txt ): "))
        type_object = int(input("write type object: "))
        create_object(name_object, type_object)
    if command == "create_user":
        create_user()
    if command == "login_user":
        login_user()
    if command == "logout_user":
        logout_user()
    if command == "refactor_type_object":
        filename = input("write filename:")
        refactor_type_object(filename, login)
    if command == "remove_file":
        filename = str(input("write name file: "))
        remove_file(filename, login)
    if command == "write_file":
        filename = str(input("write name file: "))
        message = str(input("write message: "))
        write_file(filename, message, login)
    if command == "read_file":
        filename = str(input("write name file: "))
        read_file(filename, login)
    if command == "print_lists":
        print_lists()
    if command == "clear_file":
        filename = str(input("write name file: "))
        clear_file(filename, login)
    if command == "help":
        help()


def executor():
    get_data_from_users_json()
    while True:
        print(f"-------------- {login} -----------------")
        temp_question = int(input("want to quit?(1)Yes(2)No: "))
        if temp_question == 2:
            command = str(input("write command: "))
            command_executor(command)
        if temp_question == 1:
            break
        if temp_question != 2 and temp_question != 1:
            print("Incorrect data")
            break


executor()
