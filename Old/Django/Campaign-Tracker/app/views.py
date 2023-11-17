from django.shortcuts import render

# Create your views here.
from .models import *

from .serializers import *


from rest_framework import generics


class Producrlist(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class = Product_Serializer

class CategorieList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class = Product_Serializer

class MediumList(generics.ListAPIView):
    queryset=Medium.objects.all()
    serializer_class = Medium_z