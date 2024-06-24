# example/urls.py
from django.urls import path

from coopApp.views import *


urlpatterns = [
    path('', index),
    path('about', about),
]
