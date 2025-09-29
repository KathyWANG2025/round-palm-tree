# class, init
print('\n\n-----OOP restaurant -----')
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe restaurant is " + self.restaurant_name)
        print('The cuisine type is: ' + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name + ' is open')
    def show_number_served(self):
        print('Today we have served ' + str(self.number_served) + ' customers')
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, numbs):
        self.number_served += numbs


my_restaurant = Restaurant('bistro', 'muffins')
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(10)
my_restaurant.show_number_served()
my_restaurant.increment_number_served(2)
my_restaurant.show_number_served()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = ['strawberry', 'vanilla','chocolate']
    def show_flavour(self):
        message_1 = "This ice cream stand offers the following flavours:"
        print(message_1)
        for flavour in self.flavour:
            print('\t-' + flavour)
my_icecream = IceCreamStand('Glatto', 'ice cream')
my_icecream.show_flavour()


print('\n\n-----OOP class User -----')
class User():
    def __init__(self, first_name, last_name, *user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
    def describe_user(self):
        print('\nThe user name is ' + self.first_name.title() + ' ' + self.last_name.title())
        print(self.first_name.title() + ' has the following details: '+ str(self.user_info))
    def greet_user(self):
        print('\nWelcome back, ' + self.first_name.title() + '!')
user_1 = User('jackie', 'chen', 'favorite color is red', '25 years old')
user_1.describe_user()
user_1.greet_user()

print('\n\n-----car class  -----')
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def describe_car(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name)
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_used_car = Car('honda', 'mustang', 2019)
my_used_car.update_odometer(2350000)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print('\n\n-----OOP User log in  -----')
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('\nThe user name is ' + self.first_name.title() + ' ' + self.last_name.title())
    def greet_user(self):
        print('\nWelcome back, ' + self.first_name.title() + '!')
    def read_login_attempts(self):
        print('\nYou have logged in ' + str(self.login_attempts) + ' times')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

print('\n\n-----OOP User privileges  -----')
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("The functions of Admin users are: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user_1 = User('kathy', 'wang')
user_1.describe_user()
user_1.read_login_attempts()
user_1.increment_login_attempts()


user_2 = Admin('robot', 'adminnn')
user_2.privileges.show_privileges()


print('\n\n-----E car class  -----')
class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('\nThe battery size is: ' + str(self.battery_size) + 'kwh')
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 350
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print('\nThe battery size is updated to 85kwh!')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__( make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model 3', 2019)
my_tesla.battery.battery_size = 70
my_tesla.describe_car()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print('\n\n-----OOP import modules -----')
from collections import OrderedDict
favourite_languages = OrderedDict()
favourite_languages['jen'] = 'English'
favourite_languages['franklyn'] = 'swedish'
favourite_languages['alonso'] = 'Spanish'
for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
          language.title())


print('\n\n-----OOP import modules -----')
from random import randint
x = randint(1,6)

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))

my_die_6 = Die()
print("\nThe random result of a 6-side die is: ")
for _ in range(10):
    my_die_6.roll_die()

print("\nThe random result of a 10-side die is: ")
my_die_10 = Die (10)
for _ in range (10):
    my_die_10.roll_die()


