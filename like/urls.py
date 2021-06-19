from django.urls import path
from . import views

urlpatterns = [
    path('like/', views.LikeCreateView.as_view()),
    path('dislike/', views.DisLikeCreateView.as_view()),
]