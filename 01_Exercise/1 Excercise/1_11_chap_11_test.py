# test unit test
from name_function import get_formated_name
print("Enter 'q' to quit")
while True:
    first = input("enter first name: ")
    if first == "q":
        break
    last = input("enter last name: ")
    if last == "q":
        break
    get_formated_name(first, last)
    print("Hello " + get_formated_name(first, last))
