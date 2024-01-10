from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        field = ('name', 'description')
