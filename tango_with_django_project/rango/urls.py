from django.urls import path
from rango import views

urlpatterns = [
    path(r'index', views.index, name='index'),
    path(r'^category/(?P<category_name_slug>[\w\-]+)$',
         views.show_category, name='show_category')
]