from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = ''),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('my-login/', views.my_login, name = 'my-login'),
    path('register/', views.register, name = 'register'),
]