from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from comments import serializers
from comments.models import Feedback
from comments.permissions import IsOwnerOrReadOnly
from products.models import Product
from products.serializers import ProductFeedbackSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedbackDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFeedbackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Feedback.objects.all()
#     serializer_class = serializers.FeedbackSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
