from django.urls import path

from .views import ProductVieSet, UserAPIView

urlpatterns = [
    path('products', ProductVieSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductVieSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())
]
