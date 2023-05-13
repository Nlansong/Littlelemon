from django.http import path
from . import views

urlspattern = [
    path('', views.index),
]