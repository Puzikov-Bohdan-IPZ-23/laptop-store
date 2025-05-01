from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # додай

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('laptop_list')),  # головна сторінка → список ноутбуків
    path('', include('shop.urls')),  # обов’язково після redirect
]

