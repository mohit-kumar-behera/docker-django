from django.urls import path
from . import views

app_name = 'templ'

urlpatterns = [
    path('capabilities/', views.get_capabilities_api_handler, name='get_capabilities'),
    path('templates/', views.templates_api_handler, name='get_templates'),
    path('create_template/', views.templates_api_handler, name='create_template')
]