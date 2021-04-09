"""django_bt_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
#from bt_site.views import all_users_bt
# from bt_site.views import displayAll
# from bt_site.views import friendship_add_friend
from django.contrib.auth.decorators import login_required

from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('bt_site.urls')),
    #url(r'^friendship/users/$', view=all_users_bt, name="friendship_view_users"),
    # url(r'^friendship/users/$', login_required(displayAll.as_view()), name="friendship_view_users"),
    # url(r'^friendship/friend/add/(?P<to_username>[\w-]+)/$', view=friendship_add_friend, name="friendship_add_friend"),
    # url(r'^friendship/', include('friendship.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)