from authapp import models
from django.http import HttpResponseForbidden

# custom middleware class for token validation.
from authapp.models import AccessToken

class CustomTokenAuthentication(object):

	def process_request(self, request):

		access_token = request.META.get('HTTP_AUTHORIZATION', '')
		if AccessToken.objects.filter(token=access_token).exists()
			return None
		else:
			return HttpResponseForbidden()


