from django.urls import path

from like import views
from like.views import add_like, add_dislike

urlpatterns = [
    path('', views.LikeView.as_view()),
    path('add-like/<int:pk>/', add_like),
    path('add-dislike/<int:pk>/', add_dislike),
]
