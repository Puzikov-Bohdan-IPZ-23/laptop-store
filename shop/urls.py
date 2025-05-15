from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('laptops/', views.laptop_list, name='laptop_list'),
    path('laptops/<int:pk>/', views.laptop_detail, name='laptop_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:pk>/', views.cart_remove, name='cart_remove'),
]
