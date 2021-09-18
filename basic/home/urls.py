from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('ui/', views.ui_view, name='ui'),
]