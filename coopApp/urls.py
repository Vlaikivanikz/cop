# example/urls.py
from django.urls import path

from coopApp.views import index


urlpatterns = [
    path('', index),
]
