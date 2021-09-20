from django.urls import path
from . import views

app_name = 'templ'

urlpatterns = [
    path('capabilities/', views.get_capabilities_api_handler, name='get_capabilities'),
    path('templates/', views.get_templates_api_handler, name='views.get_templates')
]