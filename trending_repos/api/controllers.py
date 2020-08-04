import requests
import datetime

def date_from_last_30():
	"""
	    Returns date from last 30 days as string
	"""

	date = datetime.datetime.now() - datetime.timedelta(days=30)  # date string n the last 30 days ( from now )

	return date.strftime('%Y-%m-%d')                              # YYYY-MM-DD format

class  APIController:
	"""
	   Wrapper for handling the API Controllers
	"""

	def __init__(self):
		self.api_data = self.get_repo_data_from_github()
		self.shortened_data = list(self.get_shortened_repo_data())
		self.languages = self.get_languages_from_data()

	def get_repo_data_from_github(self):
		"""
	        Fetches the most starred repos created in the last 30 days
	        and returns data as json
	    """
		max_items = 100
		start_date = date_from_last_30()

		api_endpoint = f"https://api.github.com/search/repositories?q=created:>{start_date}&sort=stars&order=desc"

		data = requests.get(api_endpoint).json()

		# return only relevant data
		return data.get("items")[:max_items]

	def get_shortened_repo_data(self):
		"""
	        Gets repo name,language url from each object in the data
	        Returns generator object in the form [(name,url)...(name,url)]
	    """

		items = map(lambda obj:(obj.get("name"),obj.get("languages_url")),self.api_data)

		return items

	def get_languages_from_data(self):
		"""
	        Gets languages from urls and returns results as a set
	    """

		self.item_languages = {}
		set_languages = set()                                        # cant hold duplicates
		for item in self.shortened_data:

			languages = list(requests.get(item[1]).json().keys())    # get respective languages from language_url
			self.item_languages.update({item[0]:languages})

			languages = set(languages)                               # convert languages to set
			set_languages = set_languages.union(languages)           # find union,remove duplicates

		return set_languages

	def get_list_and_number_of_repos(self):
		"""
		    Returns object containing languages and corresponding repos
	    """

		languages = list(self.languages)                                        # ['Java'...'Python']
		data_dictionary = dict(zip(languages, ([] for language in languages)))  # {'Java':[]...'Python':[]}

		for key,list_value in self.item_languages.items():
			for language in list_value:
				data_dictionary[language].append(key)

		return data_dictionary                                                  # {"Java":[repo_name,..]}

	def get_consolidated(self):
		"""
		    Returns consolidated number of repos using a language and list of repos using a language
	    """

		consolidated = {}
		data = self.get_list_and_number_of_repos()
		for key in data:
			consolidated[key] = {"Number of repos":data[key].__len__(),"List of repos":data[key]}

		return consolidated
