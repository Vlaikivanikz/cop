from django.urls import path, re_path

from coopApp.views import *
from . import views, dbreqs

urlpatterns = [
    path('', views.homepage),
    path('homepage', views.homepage),
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
    re_path(r'^getCommentsByPortId__', views.getCommentsByPortId),
    re_path(r'^css__', tools.getCss),
    re_path(r'^img__', tools.getImg),
    path('signup', views.signUp),
    re_path(r'^isThisEmailRegistered__', dbreqs.ifEmail),
    re_path(r'^isThisUserRegistered__', dbreqs.ifUser),
    path('createUser', dbreqs.createUser),
    path('login', views.login),
    path('check', dbreqs.check)
]
