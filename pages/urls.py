from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('camera', views.camera, name='camera'),
    path('result', views.result, name='result'),
    path('screenshot', views.screenshot, name='screenshot'),
]
