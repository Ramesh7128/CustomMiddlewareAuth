from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AccessToken(models.Model):

	# Model for list of valid access tokens

	token = models.CharField(max_length=40,blank=False, null=False)

	def __unicode__(self):
		return self.token


class SampleProduct(models.Model):

	# Model for sample data to return, when request has a valid token.
	
	item = models.CharField(max_length=100, blank=False, null=False)
	price = models.FloatField(blank=False, null=False)

	def __unicode__(self):
		return self.item



