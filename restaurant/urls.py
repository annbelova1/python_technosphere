from django.urls import path
from . import views
from .views import DishView


urlpatterns = [
    path('', views.dish_list, name='dish_list'),
    path('dishes/', DishView.as_view()),
    path('dishes/<int:pk>', DishView.as_view())
]