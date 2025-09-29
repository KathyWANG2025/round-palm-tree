"""

print('\n\n-----deal with errors -----')
print('enter q to quit.')

while True:
    first_number = input('Enter a first number: ')
    if first_number == 'q':
        break
    second_number = input('Enter a second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by zero')
    else:
        print(answer)
"""

print('\n\n-----alice wonderland file  -----')
file_name = input('Enter a file name: ')
try:
    with open(file_name) as f_obj:
        content = f_obj.read()
except:
    msg = "file cannot be found"
    print(msg)
else:
    words = content.split()
    num_words = len(words)
    print('There are', num_words, 'words in the file' + file_name)

print('\n\n-----Function  alice wonderland file  -----')
def count_words(file_name):
    try:
        with open(file_name) as f_obj:
            content = f_obj.read()
    except:
        msg = "file: " + file_name + "cannot be found"
        print(msg)
    else:
        words = content.split()
        num_words = len(words)
        print('There are', num_words, 'words in the file' + file_name)
count_words('guest.txt')

print('\n\n-----Function  alice wonderland file  -----')
file_names = ['guest.txt','pi_digits.txt', 'alice.txt', 'programming.txt']
for file_name in file_names:
    count_words(file_name)

print('\n\n-----Function  try error  -----')
while True:
    inp_1 = input('Enter a first number: ')
    inp_2 = input('Enter a second number: ')
    if inp_1 == 'q' or inp_2 == 'q':
        break
    try:
        num_1 = int(inp_1)
        num_2 = int(inp_2)
        out = num_1 + num_2
    except ValueError:
        msg = "incorrect input"
        print(msg)
    else:
        print(out)
