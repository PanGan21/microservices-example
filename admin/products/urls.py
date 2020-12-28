from django.contrib import admin
from django.urls import path

from .views import ProductVieSet

urlpatterns = [
    path('products', ProductVieSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductVieSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]