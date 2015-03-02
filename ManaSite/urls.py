from django.conf.urls import patterns, include, url
from django.contrib import admin
from post.views import HomePageView

urlpatterns = patterns('',
                       url(r'^$', HomePageView.as_view(), name='home'),
                       url(r'^beers/', include('beer.urls')),
                       url(r'^post/', include('beer.urls')),
                       url(r'^admin/', include(admin.site.urls))
                       , )