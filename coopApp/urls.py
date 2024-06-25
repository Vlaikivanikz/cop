from django.urls import path

from coopApp.views import *
from . import views

urlpatterns = [
    path('', views.homepage),
    path('getPorts', views.getPorts),
    path('portfolios', views.portfolios),
    path('createPort', views.createPort),
    path('creation', views.creation)
]
