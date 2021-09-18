from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.ui_view, name='ui'),
]