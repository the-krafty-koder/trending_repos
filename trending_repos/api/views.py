from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.controllers import *

api_controller = APIController()

class LanguageListView(APIView):
	"""
	    Lists the languages used by the 100 trending public repos on GitHub.
	"""

	renderer_classes = [JSONRenderer]

	def get(self,request):
		data = [key for key in api_controller.languages]        # retrieve languages
		data_obj = {'languages-used':data}
		return Response(data_obj)

class LanguageAttributesView(APIView):
	"""
	    Lists the languages used by the 100 trending public repos on GitHub.
	"""

	renderer_classes = [JSONRenderer]

	def get(self,request):
		data =  api_controller.get_consolidated()     # retrieve languages
		data_obj = {'language-attributes':data}
		return Response(data_obj)
		
