from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from .models import AccessToken
from random import randint
# from mock import Mock
from authapp.middleware.custom_token_validation import CustomTokenAuthentication

# Create your tests here.


class RequestTokenTests(TestCase):


	# Test to check when no token present in the request header
	def test_notoken_present(self):

		resp = self.client.get(reverse('productlist'))
		self.assertEqual(resp.status_code, 401)


	# Test to check if a valid token present in the request header
	def test_invalid_token_present(self):
		resp = self.client.get(reverse('productlist'), **{'HTTP_TOKEN':'8742627sdfsdfsf4e3423dsd23'})
		self.assertEqual(resp.status_code,200) 


	# Test to check if an invalid token passed in request header
	def test_invalid_token_present(self):
		resp = self.client.get(reverse('productlist'), **{'HTTP_TOKEN':'39282983923'})
		self.assertEqual(resp.status_code,401)



