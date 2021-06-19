from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodListView.as_view()),
    path('<int:pk>/', views.FoodDetailView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('search/', views.FoodListView.as_view()),
    path('create/', views.FoodCreateView.as_view()),
    path('update/<int:pk>/', views.FoodUpdateView.as_view()),
    path('delete/<int:pk>/', views.FoodDestroyView.as_view())
]
