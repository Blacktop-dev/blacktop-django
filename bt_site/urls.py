from django.conf.urls import url, include
from friendship.views import all_users

from . import views
from .views import sent_success, add_friendteetime, accept_teetime_request, message_view, sent_failure
from django.contrib.auth.decorators import login_required

app_name = 'bt_site'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^add_tee_time/$', views.AddShuttleView.as_view(), name='shuttle_tee_time'),
    url(r'^find_rides/$', views.FindRidesView.as_view(), name='find_rides'),
    url(r'^my_tee_times/$', views.MyTeeTimesView.as_view(), name='my_tee_times'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^sent/success/$', view=sent_success, name='sent_success'),
    #url(r'^add/teetime/(?P<to_username>[\w-]+)/(?P<to_teetime>[\w-]+)/$', view=add_friendteetime, name="add_friendteetime"),
    url(r'^add/teetime/(?P<to_teetime>[\w-]+)/$', view=add_friendteetime, name="add_friendteetime"),
    url(r'^accept/teetimerequest/(?P<to_username>[\w-]+)/(?P<to_teetime>[\w-]+)/$', view=accept_teetime_request, name="accept_teetime_request"),
    url(r'^socialpage/$', views.SocialView.as_view(), name="social_page"),
    url(r'^message/(?P<to_user>[\w-]+)/$', view=message_view, name="message"),
    url(r'^sent/failure/$', view=sent_failure, name='sent_failure'),
]
