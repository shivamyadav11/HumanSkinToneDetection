from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('verify', views.verify, name='verify'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
