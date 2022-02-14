from django.urls import path
from . import views

app_name = 'poems'

urlpatterns = [
    path('', views.index, name='index'),
]
