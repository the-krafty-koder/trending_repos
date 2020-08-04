from django.test import TestCase
from .controllers import *

# Create your tests here.

class TestContollers(TestCase):
	"""
	    Tests for functions in controllers.py
	"""
	
	def setUp(self):
		self.controller = APIController()

	def test_date_from_last_30(self):
		date = date_from_last_30()
		self.assertEqual('2020-07-05',date)

	def test_get_repo_data_from_github(self):
		self.assertTrue(self.controller.api_data)

	def test_get_shortened_repo_data(self):
		data = self.controller.shortened_data
		self.assertTrue(data)

	def test_get_languages_from_data(self):
		languages = self.controller.languages
		self.assertIn("JavaScript",languages)
	
	def test_get_list_and_number_of_repos(self):
		self.assertTrue(self.controller.get_list_and_number_of_repos())




		

