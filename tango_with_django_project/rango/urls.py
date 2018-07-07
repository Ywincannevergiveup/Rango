from django.urls import re_path
from rango import views

urlpatterns = [
    re_path('index/', views.index, name='index'),
    re_path('add_category/', views.add, name='add_category'),
    re_path('add_page/(?P<category_name_slug>[\w\-]+)/', views.add_page, name='add_page'),
    re_path('category/(?P<category_name_slug>[\w\-]*)',
         views.show_category, name='show_category'),
]
