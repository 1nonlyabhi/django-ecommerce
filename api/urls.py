from turtle import home
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
]