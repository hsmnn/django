from django.urls import path
from django.urls import path
from . import views

app_name = 'names'
urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('generate', views.IndexView.generate, name="generate"),
]