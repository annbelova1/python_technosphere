from django.urls import path, include
from . import views
from .views import DishView
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("home", views.home, name="home"),
    path("dish_list", views.dish_list, name="dish_list"),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('new', views.dish_create, name='dish_new'),
    path('edit/<int:pk>', views.dish_update, name='dish_edit'),
    path('delete/<int:pk>', views.dish_delete, name='dish_delete'),
    path('dishes/', DishView.as_view()),
    path('dishes/<int:pk>', DishView.as_view())
]