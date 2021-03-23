from django.conf.urls import url, include

from . import views

app_name = 'bt_site'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^display/$', views.Display.as_view(), name='display'),
    url(r'^friendrequest/$', views.FriendRequestView.as_view(), name='friendrequest'),
    #url(r'^friendship/', include('friendship.urls')),
]