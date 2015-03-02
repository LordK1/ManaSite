from django.conf.urls import patterns, url

__author__ = 'k1'

urlpatterns = patterns('',
                       url(r'^list/$', PostListView.as_view(), name='post-list'),
                       url(r'^(?P<slug>[-\w+])/$', PostDetailView.as_view(), name='post-detail'),
                       url(r'^categories/$', CategoryListView.as_view(), name='category-list'),
                       url(r'^category/(?P<slug>[-\w+])$', CategoryDetailView.as_view(), name='category-detail')
                       ,)