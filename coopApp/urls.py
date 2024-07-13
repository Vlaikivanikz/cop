from django.urls import path, re_path

from coopApp.views import *
from . import views

urlpatterns = [
    path('', views.homepage),
    path('getPorts', views.getPorts),
    path('portfolios', views.portfolios),
    path('createPort', views.createPort),
    path('creation', views.creation),
    re_path(r'_&&port\Z', views.creation),
    re_path(r'^getOnePort__', views.getPortById),
    re_path(r'^editPort__', views.editPort),
    path('delete', views.deleteAll),
    path('find', views.search),
    re_path(r'^deleteOne_', views.deleteOne),
    path('sendComment', views.sendComment),
    re_path(r'^getCommentsByPortId__', views.getCommentsByPortId)
]
