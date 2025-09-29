car = 'subaru'
print(car == 'subaru')
print(car == 'audi')

name = 'Sarah'
print(name.lower())
print(name.upper())
lowername = 'sarah'
print(lowername == name.lower())

print('----------')
drinks = ['coffee', 'milk','Coke','juice']
mydrink = 'latte'
if mydrink not in drinks:
    print(mydrink.upper() + ' is not in the list of drinks, Please refill')

"""
aliens color
"""

print('----now is the trick for games------')
alien_color = 'red'
if alien_color == 'green':
    print('You got 5 points')
elif alien_color == 'yellow':
    print('You got 10 points')
else:
    print('You got 15 points')

print('----now is the trick for website and users------')
usernames = ['admin','sarah','jack','kathy','mickel','koby']
admin = 'admin'
if not usernames:
    print('We need to find some users!')
else:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello! ' + username + ', thank you for logging in again.' )

print('----now is the trick for website and new users------')
current_users = ['yammy','sarah','Jack','kathy','koby']
lowercase_current_users = [name.lower() for name in current_users]
new_users = ['jack','Sarah','winsky','Jordan','David']
for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print('name: ' + new_user.title() + ' used, type a new name.')
    else:
        print('Good name!  ' + new_user.title() )