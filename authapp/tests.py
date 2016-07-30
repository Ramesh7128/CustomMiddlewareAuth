from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from .models import AccessToken
from random import randint
from mock import Mock
from authapp.middleware.custom_token_validation import CustomTokenAuthentication
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test.client import Client
c = Client()
import requests

url = "https://headertokenauth.herokuapp.com/"


# Create your tests here.


class RequestTokenTests(TestCase):

	def setUp(self):
		self.middleware = CustomTokenAuthentication()
		
	# Test to check when no token present in the request header
	def test_notoken_present(self):

		resp = self.client.get(reverse('productlist'))
		self.assertEqual(resp.status_code, 401)


	# Test to check if a valid token present in the request header
	def test_valid_token_present(self):
		headers = {
    	'token': "46cf9aa67fc14e74a7cb5b3e8dd74ec6",
    	}
		response = requests.request("GET", url, headers=headers)
		self.assertEqual(response.status_code,200) 


	# Test to check if an invalid token passed in request header
	def test_invalid_token_present(self):
		headers = {
    	'token': "invalid_token",
    	}
		response = requests.request("GET", url, headers=headers)
		self.assertEqual(response.status_code,401)


