from django.conf.urls import url, include
from friendship.views import all_users

from . import views

app_name = 'bt_site'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^display/$', views.Display.as_view(), name='display'),
    url(r'^friendrequest/$', views.FriendRequestView.as_view(), name='friendrequest'),
    #url(r'^test/(?P<template_name>\d+)/$', view=all_users, name='test'),
    #url(r'^makefriends/(?P<string>[\w\-]+)/$', view=all_users, name="makefriends"),
    #url(r'^friendship/', include('friendship.urls')),
]