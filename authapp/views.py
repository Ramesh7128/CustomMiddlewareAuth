from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import SampleProduct
from .serializers import SampleProductSerializer
# Create your views here.


class ProductList(APIView):


	def get(self, request):
		products = SampleProduct.objects.all()
		serializer = SampleProductSerializer(products, many=True)
		return Response(serializer.data)


	def post(self):
		pass