# 文件、错误处理，json
from symbol import return_stmt

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print("contents are: " + contents)
with open('pi_digits.txt') as file_object:
    for line in file_object.readlines():
        print("lines are: " + line.rstrip())
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip().strip()
print(pi_string[:15])
print(len(pi_string))

birthday_1 = '19990213'
birthday_2 = '15926535'
print(birthday_1 in pi_string)
print(birthday_2 in pi_string)

print('\n\n-----Read files -----')
with open('learning_python.txt') as python_file_object:
    python_contents = python_file_object.read()
    print(python_contents)
with open('learning_python.txt') as python_file_object:
    for line in python_file_object.readlines():
        print(line.rstrip())
with open('learning_python.txt') as python_file_object:
    python_lines_all = python_file_object.readlines()
python_lines = []
for python_line in python_lines_all:
    python_line = python_line.rstrip()
    python_lines.append(python_line)
    print(python_line)

print('\n\n-----rewrite files -----')
with open('learning_python.txt') as python_file_object:
    python_lines_all = python_file_object.readlines()
python_lines = []
for python_line in python_lines_all:
    python_line = python_line.rstrip()
    python_lines.append(python_line)
    print(python_line.replace('Python', 'C'))

print('\n\n-----write files -----')
with open('programming.txt', 'w') as write_file_object:
    write_file_object.write('Python is a programming language\n')
    write_file_object.write('This language is somewhat easy\n')

with open('programming.txt', 'a') as write_file_object:
    write_file_object.write('Python is not erased')

print('\n\n-----write files Exercise -----')
user_name = input('Enter a username: ')
with open('guest.txt', 'w') as guest_file_object:
    guest_file_object.write(user_name)
print('finish writing user name')

print('\n\n-----write files with while Exercise -----')
user_name = input('Enter a username: ')
with open('guest_book.txt', 'a') as guest_book_file_object:
    while user_name != 'Finish entering':
        guest_book_file_object.write(user_name + '\n')
        print('Hello !' + user_name)

        user_name = input('Enter a username: ')
print('Finish entering')



