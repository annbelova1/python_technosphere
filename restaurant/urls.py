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
    path("", views.home, name="home"),
    path('', views.dish_list, name='dish_list'),
    path('dishes/', DishView.as_view()),
    path('dishes/<int:pk>', DishView.as_view())
]