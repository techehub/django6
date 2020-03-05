from django.contrib import admin
from django.urls import path
from .views import displayProduct, displayProductList

urlpatterns = [
    path('product/<str:pid>', displayProduct),
    path('productlist/', displayProductList),
]
