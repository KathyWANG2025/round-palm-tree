# json.dump & load
"""

import json
numbers = [2,3,5,7,11,13]
filname = 'numbers.json'
with open(filname, 'w') as f_object:
    json.dump(numbers, f_object)

with open(filname) as f_object:
    numbers = json.load(f_object)
    print(numbers)

print("json -----remember user me")
import json
username = input('Enter a username: ')
filname = 'username.json'
with open(filname, 'w') as f_object:
    json.dump(username, f_object)
    print("We'll remember your username" + username + "!")

"""

import json
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Enter a username: ')
    filename = 'username.json'
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(username + " wellcome!")
    else:
        username = get_new_username()
        print("We well remember your username " + username + "!")

greet_user()

