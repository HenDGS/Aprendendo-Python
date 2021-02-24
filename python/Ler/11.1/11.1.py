import unittest
from city_functions import geo

class NamesTestCase(unittest.TestCase):
	def test_city_country(self):
		nomes=geo("curitiba","brasil")
		self.assertEqual(nomes,"curitiba,brasil - população ")
	
unittest.main()
