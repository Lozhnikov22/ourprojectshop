from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from category.models import Category
from category.serializers import CategorySerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer