from django.conf.urls import path
from home.api import views

app_name = 'docker_api'

urlpatterns = [
    path('create-docker/', views.create_docker_api_handler, name='create_docker'),
    path('scan-docker/', views.scan_docker_api_handler, name='scan_docker'),
]