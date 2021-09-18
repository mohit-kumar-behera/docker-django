from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.ui_view, name='ui'),
    path('create-docker', views.create_docker_api_handler, name='create_docker')
]