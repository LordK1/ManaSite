from django.conf.urls import patterns, url

from community.views import LikePostView, DisLikePostView, FollowAuthorView


__author__ = 'k1'

urlpatterns = patterns('',
                       url(r'^like/(?P<pk>\d+)/$', LikePostView.as_view(), name='like-post'),
                       url(r'^dislike/(?P<pk>\d+)/$', DisLikePostView.as_view(), name='dislike-post'),
                       url(r'^follow/(?P<pk>\d+)/$', FollowAuthorView.as_view(), name='follow-author'),
                       )