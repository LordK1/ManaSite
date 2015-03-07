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
                       # Overridden Login Page
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'author/login.html'},
                           name='login'),
                       # # Overridden LogOut Page
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout')
                       ,) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)