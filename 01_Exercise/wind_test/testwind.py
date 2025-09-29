from WindPy import w

w.start()

wind_data = w.wset("indexconstituent","date=2025-09-29;windcode=899050.BJ")
print(wind_data)