from django.urls import path
from . import views

app_name = 'cauban_sample'  

urlpatterns = [
    path('', views.index, name='index'),
]