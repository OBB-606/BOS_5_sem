"""
Система военных сообщений
Управление доступом на основе ролей.
Контейнер - словарь, где ключ - название объекта, значение_1 - метка конфиденциальности контейнера, зн_2 - список объектов
Типы объектов: public, secret, top_secret, special
Типы субъектов: R, S, L, graph, root
"""
import csv
import json
import os
import sys

users_dict: dict = {}  # Словарь с информацией субъектов
actions_dict: dict = {}  # Словарь действий за текущую сессию
containers_dict: dict = {}  # Словарь контейнеров


def help():
    print("command's : "
          "remove_file - удалить файл\n"
          "read_file - прочитать файл\n"
          "write_file - вписать в файл\n"
          "clear_file - удалить содержимое файла\n"
          "logout_user - логаут\n"
          "refactor_role - поменять роль у субъекта\n"
          "refactor_type_object - поменять метку конфиденциальности объекта\n"
          "create_object - создать объект\n"
          "create_user - создать субъекта\n"
          "login_user - зайти в систему под другим пользователем\n"
          "print_lists - вывести список существующих пользователей системы\n"
          "")


def save_actions_file():
    with open("actions.json", "w") as json_file:
        json.dump(actions_dict, json_file, indent=2)


def save_users_file():
    with open("users.json", 'w') as json_file:
        json.dump(users_dict, json_file, indent=2)


def check_right(filename: str, user: str):  # проверка прав доступа у субъекта на объект
    flag = False
    if users_dict["users"][user] == "R" and users_dict["objects"][filename] == "public":
        flag = True
    if users_dict["users"][user] == "S" and users_dict["objects"][filename] == "secret":
        flag = True
    if users_dict["users"][user] == "L" and users_dict["objects"][filename] == "top_secret":
        flag = True
    if users_dict["users"][user] == "graph" and users_dict["objects"][filename] == "special":
        flag = True
    return flag


def first_check_right(type_object: str, user: str):  # первая проверка прав доступа у субъекта на объект
    flag = False
    if users_dict["users"][user] == "R" and type_object == "public":
        flag = True
    if users_dict["users"][user] == "S" and type_object == "secret":
        flag = True
    if users_dict["users"][user] == "L" and type_object == "top_secret":
        flag = True
    if users_dict["users"][user] == "graph" and type_object == "special":
        flag = True
    return flag


def remove_file(filename: str, user: str):
    if user == "root":
        try:
            os.remove(filename)
        except IOError:
            print("Файл отсутствует!")
    else:
        if check_right(filename, user) is True:
            try:
                os.remove(filename)
            except IOError:
                print("Файл отсутствует!")
            actions_dict[user]["objects"].append(f"Remove object {filename}")
            save_actions_file()
        else:
            print("You are not authorized for this action!")
            executor()


def clear_file(filename: str, user: str):
    if user == "root":
        try:
            with open(filename, "w") as c_f:
                pass
        except IOError:
            print("IO Error!")
    else:
        if check_right(filename, user) is True:
            try:
                with open(filename, "w") as c_f:
                    pass
            except IOError:
                print("IO Error!")
            actions_dict[user]["objects"].append(f"Clear_object {filename}")
            save_actions_file()
        else:
            print("You are not authorized for this action!")
            executor()


def write_file(filename: str, message: str, user: str):
    if user == "root":
        try:
            handle = open(filename, 'a')
            handle.writelines(message)
        except IOError:
            print("IO Error!")
        finally:
            handle.close()
    else:
        if check_right(filename, user) is True:
            try:
                handle = open(filename, 'a')
                handle.writelines(message)
            except IOError:
                print("IO Error!")
            finally:
                handle.close()
            actions_dict[user]["objects"].append(f"Write in object {filename}")
            save_actions_file()
        else:
            print("You are not authorized for this action!")
            executor()


def refactor_role(user_1: str, user_2: str):
    if user_1 == "root":
        new_role = input("write new role for this subject: ")
        users_dict["users"][user_2] = new_role
        save_users_file()
    else:
        print("You are not authorized for this action!")
        executor()


def refactor_type_object(filename: str, user: str):
    if user == "root":
        new_type_object = input("write new type this object: ")
        users_dict["objects"][filename] = new_type_object
        save_users_file()

    else:
        print("You are not authorized for this action!")
        executor()


def create_container(user: str):
    global containers_dict
    container: list = []
    name_container = input("write_name_container: ")
    containers_dict[name_container] = {}
    count_objects = int(input("write count objects in container: "))
    for i in range(count_objects):
        temp_name_object = input(f"write {str(i + 1)}'th name object:")
        container.append(temp_name_object)
        containers_dict[name_container]["objects"] = container

    dict_values: dict = {
        "public": 0,
        "secret": 1,
        "top_secret": 2,
        "special": 3
    }

    dict_keys: dict = {
        0: "public",
        1: "secret",
        2: "top_secret",
        3: "special"
    }
    temp_list = []
    temp_list_2 = []
    for i in container:
        temp_list.append(users_dict["objects"][i])
    for i in temp_list:
        temp_list_2.append(dict_values[i])
    type_container = max(temp_list_2)
    containers_dict[name_container]["type"] = dict_keys[type_container]
    print(f"Был создан контейнер {name_container} с типом {containers_dict[name_container]['type']}")
    actions_dict[user]["containers"].append(f"Create container {name_container} with type {containers_dict[name_container]['type']}")
    save_actions_file()


def read_file(filename: str, user: str):
    if user == "root":
        try:
            handle = open(filename, "r")
            print(handle.read())
        except IOError:
            print("File is not found!")
        finally:
            handle.close()
    else:
        temp = check_right(filename, user)
        if temp is True:
            try:
                handle = open(filename, "r")
                print(handle.read())
            except IOError:
                print("File is not found!")
            finally:
                handle.close()
            actions_dict[user]["objects"].append(f"Read object {filename}")
            save_actions_file()
        else:
            print("You are not authorized for this action!")
            executor()


def logout_user():
    sys.exit()


def create_object(filename: str, user: str):
    type_object = input("write type object: ")
    temp = first_check_right(type_object, user)
    if temp is True:
        handle = open(filename, "w")
        handle.write("")
        handle.close()
        users_dict['objects'][filename] = type_object
        actions_dict[user]["objects"].append(f"Create object {filename} with type {type_object}")
        save_users_file()
        save_actions_file()
    else:
        print("You are not authorized for this action!")
        executor()


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
    actions_dict[login] = {"commands": [],
                           "objects": [],
                           "containers": []
                           }
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
actions_dict[login] = {"commands": [],
                       "objects": [],
                       "containers": []
                       }


def create_user():  # создавать субъектов может только root
    global login_list, password_list, login, password
    if login == "root" and password == "1234":
        login_new_user = str(input("login new user: "))
        password_new_user = str(input("password new user: "))
        if login_new_user not in login_list:
            tmp = [login_new_user, password_new_user]
            with open("login_password.csv", 'a', newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(tmp)
            type_user = input("write type user: ")
            users_dict["users"][login_new_user] = type_user
            actions_dict[login_new_user] = {"commands": [], "objects": [], "containers": []}
            save_users_file()
            save_actions_file()
        else:
            print("this user is already exists")
    else:
        print("You are not authorized to do this.")
        executor()


def command_executor(command: str):
    if command == "create_object":
        name_object = str(input("write name object (with .txt ): "))
        create_object(name_object, login)
    if command == "create_user":
        create_user()
    if command == "create_container":
        create_container(login)
    if command == "refactor_role":
        temp_user = input("write user: ")
        refactor_role(login, temp_user)
    if command == "refactor_type_object":
        filename = input("write filename: ")
        refactor_type_object(filename, login)
    if command == "login_user":
        login_user()
    if command == "logout_user":
        logout_user()
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


flag = True


def executor():
    global flag
    get_data_from_users_json()
    while flag:
        print(f"-------------- {login} -----------------")
        temp_question = int(input("want to quit?(1)Yes(2)No: "))
        if temp_question == 2:
            command = str(input("write command: "))
            actions_dict[login]["commands"].append(f"Enter command: {command}")
            save_actions_file()
            command_executor(command)
        if temp_question == 1:
            flag = False
            break
        if temp_question != 2 and temp_question != 1:
            print("Incorrect data")
            break


executor()
