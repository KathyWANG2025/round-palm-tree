import unittest
from city_function import city_country_function

class CityTestCase(unittest.TestCase):
    def test_city_country_function(self):
        city_info = city_country_function('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago Chile')
unittest.main()