import unittest
from name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formated_name = get_formated_name('janis', 'joplin')
        self.assertEqual(formated_name, 'Janis Joplin')

unittest.main()
