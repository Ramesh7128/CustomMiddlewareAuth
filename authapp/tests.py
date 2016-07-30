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

# Create your tests here.


class RequestTokenTests(TestCase):

	def setUp(self):
		self.middleware = CustomTokenAuthentication()
		
	# Test to check when no token present in the request header
	def test_notoken_present(self):

		resp = self.client.get(reverse('productlist'))
		self.assertEqual(resp.status_code, 401)


	def test_process_request_with_cart(self):
		request = Mock(path='/')
		request.method = 'GET'
		request.META = {'HTTP_TOKEN': '6518907536324d17b2fff658fe545b00'}
		response = self.middleware.process_request(request)
		self.assertEqual(response.status_code, 200)

	# Test to check if a valid token present in the request header
	def test_valid_token_present(self):
		# accessToken = AccessToken.objects.all().last()
		resp = c.get(reverse('productlist'), {}, **{'TOKEN':'6518907536324d17b2fff658fe545b00', 'REMOTE_ADDR':'http://localhost:8000/'})
		# resp = self.client.get(reverse('productlist'), **{'HTTP_TOKEN':accessToken.token})
		self.assertEqual(resp.status_code,200) 


	# Test to check if an invalid token passed in request header
	def test_invalid_token_present(self):
		resp = self.client.get(reverse('productlist'), **{'HTTP_TOKEN':'39282983923'})
		self.assertEqual(resp.status_code,401)



