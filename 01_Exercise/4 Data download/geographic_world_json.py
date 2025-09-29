import json
import pygal
from pygal_maps_world.maps import World
from test_pygal import get_country_code
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        # print(country_name + ": " + str(population))
        if code:
            cc_population[code] = population
wm = World()
wm.title = 'World Population in 2010, by country code'
wm.add('2010', cc_population)

wm.render_to_file('world_population.svg')