from django.urls import path

from mainapp.views import products, main

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='index'),
    path('products/', products, name='categories'),
    path('products/<slug:pk>/', products, name='category'),
]
