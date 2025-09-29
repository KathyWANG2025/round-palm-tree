sarah = {
    'name':'Sarah Jay',
    'age':18,
    'city':'New York',}
print(sarah['name'])
print(sarah['age'])
print(sarah['city'])

for key, value in sarah.items():
    print('\nKey:', key)
    print('Value:', value)

print('\n')
print('------new game for aliens ----')
print('\n')
aliens = []
for alien_number in range(10):
    new_alien = {'alien num':alien_number,'color':'green','points':5,'speed':5}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    print(alien)
print('......')

print('\n')
print('------dict for cities ----')
print('\n')
NY = {'country':'America','population':20000,'fact':'modern city'}
Paris = {'country':'France','population':5000,'fact':'romantic city'}
Frankfurt = {'country':'Germany','population':1000,'fact':'kalt city'}
cities = {'NY':NY,'Paris':Paris,'Frankfurt':Frankfurt}

import pprint
pprint.pprint(cities)