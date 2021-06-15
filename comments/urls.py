from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedbackListCreateView.as_view()),
    path('<int:pk>/', views.FeedbackDetailView.as_view()),
]