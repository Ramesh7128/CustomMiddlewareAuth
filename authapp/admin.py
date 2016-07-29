from django.contrib import admin

# Register your models here.
from models import AccessToken, SampleProduct

admin.site.register(AccessToken)
admin.site.register(SampleProduct)