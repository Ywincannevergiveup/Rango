from django.urls import path
from rango import views

urlpatterns = [
    path(r'index', views.index, name='index'),
]