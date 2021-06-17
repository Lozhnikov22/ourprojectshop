
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, serializers, permissions

from category.models import Category
from category.serializers import CategorySerializer
from comments.permissions import IsOwnerOrReadOnly


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#
# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)