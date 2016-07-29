from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AccessTokens(models.Model):

	token = models.CharField(max_length=40,blank=False, null=False)

	def __unicode__(self):
		return self.token


