from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('ui/', views.ui_view, name='ui'),
    path('create_project/', views.create_docker_api_handler, name='create_docker'),
    path('create_compose_project/', views.compose_docker_api_handler, name='compose_docker'),
    path('scan/', views.scan_docker_file, name='scan'),
    path('scan_compose_file/', views.scan_composed_docker_file, name='scan_composed_docker'),
    path('build/', views.build_docker_file, name='build'),
]