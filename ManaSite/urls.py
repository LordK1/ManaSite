from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from post.views import HomePageView


urlpatterns = patterns('',
                       url(r'^$', HomePageView.as_view(), name='home'),
                       url(r'^post/', include('post.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^author/', include('author.urls')),
                       url(r'^account/', include('account.urls')),
                       url(r'^community/', include('community.urls'))
                       , ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)