import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CustomTokenAuth.settings")
import django
django.setup()
import uuid
from authapp.models import AccessToken


def populate():

	# Function to load AccessToken table with token value. 

	for i in range(10):
		access_token = uuid.uuid4().hex
		tokeninstance,created = AccessToken.objects.get_or_create(token=access_token)
		if not created:
			i -= 1

# Start execution here!
if __name__ == '__main__':
    populate()




