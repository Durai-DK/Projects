from rest_framework import serializers
from .models import *

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class Categories_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        depth = 1
        
class Medium_z(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = '__all__'
        depth = 2

