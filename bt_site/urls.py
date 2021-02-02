from django.urls import path

from bt_site import views

urlpatterns = [
    path('', views.index, name='index'),
]