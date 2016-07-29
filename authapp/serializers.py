from rest_framework import serializers
from .models import SampleProduct


class SampleProductSerializer(serializers.ModelSerializer):

	#Serializer for SampleProduct model. 
	class Meta:
		model = SampleProduct
		fields = '__all__'