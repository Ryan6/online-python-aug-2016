from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), # L&R - welcome
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.books), # home
    url(r'^books/(?P<id>\d+)$', views.reviews), # add review & see reviews
    url(r'^books/add$', views.add), # add book and review
    url(r'^user/(?P<id>\d+)$', views.user), # name, email, total reviews, books reviewed
    url(r'^process_add$', views.process_add),
    url(r'^logout$', views.logout),
]
