from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy)
]