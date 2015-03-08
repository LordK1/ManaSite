from django.conf.urls import patterns, url

from author.views import AuthorDetailView, AuthorListView


__author__ = 'k1'

urlpatterns = patterns('',
                       url(r'^list/$', AuthorListView.as_view(), name='author-list'),
                       url(r'^(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),)