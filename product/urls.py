from django.contrib import admin
from django.urls import path
from .views import displayProduct, displayProductList, addToCart,cart

urlpatterns = [
    path('product/<str:pid>', displayProduct),
    path('productlist/', displayProductList),
    path('addToCart', addToCart),
    path ('cart', cart)
]
