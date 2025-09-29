"""

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print('-----while function-----')
prompt = '\nEnter something:'
prompt += "\nEnter 'quit' to exit the program."
message = ""
while message != 'quit':
    message = input(prompt)
    # print(message)

    if message != 'quit':
        print(message)

print('-----while / active function-----')
# signal trur or false
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



print('\n\n-----while / pizza function-----')
pizza_promt = '\nPlease enter some pizza toppings'
pizza_promt += '\nEnter quit to exit the choosing.'
message = ""
while message != 'quit':
    message = input(pizza_promt)
    if message != 'quit':
        print('We will add ' + message + 'in your pizza order.')
    else:
        print('Thanks! order received')


print('\n\n-----while / pizza function-----')
"""

"""
unconfirmed_users = ['sarah','jack','kathy','mickel','koby']
confirmed_users = []
print(unconfirmed_users)
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('verifying user ' + current_user)
    confirmed_users.append(current_user)
print('\nthe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# mountain poll
responses = {}
polling_active = True
while polling_active:
    name = input('\nWhat is your name?')
    response = input('Which city would you like to go?')
    responses[name] = response
    repeat = input('\nWould you like to go again?')
    if repeat == 'no':
        polling_active = False
print('-----polling results-----')
for name, response in responses.items():
    print(name + 'like to climb the ' + response)

"""
sandwich_orders = ['tuna','cheese','vega','pastra']
finished_orders = []
print(sandwich_orders)
print('pastra sandwich is out of stock')
while sandwich_orders:
    order = sandwich_orders.pop()
    if order == 'pastra':
        continue
    print('I have made you order ' + order)
    finished_orders.append(order)
print('\nI have finished your sandwich orders:')
for order in finished_orders:
    print(order)