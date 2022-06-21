from django.urls import path
from .views import index_view, service_view, integrity_view

urlpatterns = [
    path('', index_view, name='index'),
    path('index.html', index_view, name='index'),
    path('service.html', service_view, name='service'),
    path('integrity.html', integrity_view, name='integrity'),
    
]