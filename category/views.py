from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from category import serializers
from category.models import Category


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer