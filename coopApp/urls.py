from django.urls import path

from coopApp.views import *
from . import views

urlpatterns = [
    path('', views.homepage),
]
