def favorite_book(book_name):
    print('My favorite book is ' + book_name +', I really recommend you read it!')
favorite_book('Gone with the wind')

def describe_pet(animal_type, name):
    """describe the pet info"""
    print('\nI have a ' + animal_type + '.')
    print('My' + animal_type + "'s name is " + name + "." )
describe_pet('dog','wikey')
describe_pet(name='loggyies',animal_type='cat')

def make_shirt(size, logo):
    print('\nI have a shirt ' + size + ' with the logo of ' + logo + '.')
make_shirt('small', 'Birthday')

# return value
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
basketball_player = get_formatted_name('koby', 'briant')
print('\n' + basketball_player)
musician = get_formatted_name('meimei', 'swift')
print('\n' + musician)

def build_person(first_name, last_name,age = ''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musical = build_person('koby', 'briant', '18')
print(musical)

def describe_city(city, country = 'US'):
    print(city + ' is in ' + country)
describe_city('Portland')
describe_city('London','England')

print('\n\n-----def replace other codings  print func -----')

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing models: ' + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print('\nThe following models are completed:')
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot', 'dodeca']
completed_models = []
unprinted_design22 = ['huawei case', 'xiaomi', 'watch case']
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_design22)

print('\n\n-----def location and other parameter -----')
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location='princeton', field='physics')
print(user_profile)

my_profile = build_profile('qiyuan','wang', birthplace = 'Tangshan', favcolor = 'orange')
print(my_profile)

print('\n\n-----def make pizza -----')
def make_pizza(*toppings):
    print('\nI will make a pizza with the toppings: ')
    for topping in toppings:
        print('-' + topping)
make_pizza('cheese','pepperoni')

print('\n\n-----def car profile -----')
def car_profile(make, model, **car_info):
    profile = {}
    profile['car_make'] = make
    profile['car_model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile
car = car_profile(make = 'subaru', model = 'outback', color = 'red', two_package = True)
print(car)