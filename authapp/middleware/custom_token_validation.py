from authapp import models
from django.http import HttpResponse

# custom middleware class for token validation.
from authapp.models import AccessToken

class CustomTokenAuthentication(object):

	def process_request(self, request):

		access_token = request.META.get('HTTP_TOKEN', '')
		if AccessToken.objects.filter(token=access_token).exists():
			return None
		else:
			res =  HttpResponse("Invalid token", status=401)
			res["WWW-Authenticate"] = "Invalid Token"
			return res



