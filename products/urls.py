from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('create/', views.ProductCreateView.as_view()),
    path('<int:pk>/', views.ProductRetrieveView.as_view()),
    path('delete/<int:pk>/', views.ProductDestroyView.as_view()),
]