import json
import prettytable

users: dict = {
    "Sanya": {"file_1":[1,1,1, "type_1"], "file_2": [1,0,0,"type_2"], "type_user": "user"},
    "Valery": {"file_3": [1, 0, 1, "type"], "type_user": "guest"}
}

# users: dict = {}
#
# for i in users:
#     print(i, users[i])
# def get_data():
#     global users
#     with open("test.json", "r") as json_file:
#         users = json.load(json_file)
#
#
# def save_data():
#     global users
#     with open("test.json", "w") as json_file:
#         json.dump(users, json_file, indent = 3)
#
#
# get_data()
# username = input("write username: ")
# filename = input("write filename: ")
# users[username][filename] = [1, 1, 1]
# save_data()

print(users)

users.clear()
print(users)
