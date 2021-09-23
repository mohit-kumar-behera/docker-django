from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('ui/', views.ui_view, name='ui'),
    path('create_project/', views.create_docker_api_handler, name='create_docker'),
    path('scan/', views.scan_docker_file, name='scan'),
    path('build/', views.build_docker_file, name='build'),
]