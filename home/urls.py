from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('ui/', views.ui_view, name='ui'),
    path('create_project/', views.create_docker_api_handler, name='create_docker'),
    path('scan/', views.scan_docker_file, name='scan'),
    path('test/', views.test_django_body, name='test'),
    
]