from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^process_money$', views.process_money),
    url(r'^reset$', views.reset)
]
