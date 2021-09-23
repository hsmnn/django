from django.urls import path
from django.urls import path
from . import views

app_name = 'names'
urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate, name="generate"),
]