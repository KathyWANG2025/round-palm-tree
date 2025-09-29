car = 'benz'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print('_________')
age = 32
if age < 4:
    price = 0
elif age < 18:
    price = 4
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

print('_________')
pizzas = ['pepperoni','cheese','Hawaii']
for pizza in pizzas:
    print("I like " +pizza + " pizza")
print('\n I really like pizza')

print('_________')
for num in range(1,21):
    print(num)


print('_________')
nums = list (range(1,1000001))
print(min(nums))
print(max(nums))
total = sum(nums)
print(total)

print('_________')
numlist_1 = list(range(1,20,2))
for i in numlist_1:
    print(i)

numlist_2 = list(range(3,31,3))
for i in numlist_2:
    print(i)

print('_________')
numlist_3 = list(value**2 for value in range(1,11))
for i in numlist_3:
    print('numlist_3: ',i)
    print(numlist_3)
numlist_4 = list()
for value in range(1,11):
    num_4 = value ** 2
    numlist_4.append(num_4)
    print('numlist_4: ',num_4)
    print(numlist_4)
print('_________')
l = int(len(numlist_3)/2 -1)
print(numlist_3)
print('The first 3 items in the numlist_3 are:', numlist_3[0:3])
print('The middle 3 items in the numlist_3 are:', numlist_3[l-1:l+2])
print('The last 3 items in the numlist_3 are:', numlist_3[-3:])