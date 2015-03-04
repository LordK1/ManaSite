from django.conf.urls import patterns, url
from author.views import ContactFormView, RegistrationFormView, AuthorProfile

__author__ = 'k1'

urlpatterns = patterns('',
                       url(r'^registration/$', RegistrationFormView.as_view(), name='author-register'),
                       url(r'^contact/$', ContactFormView.as_view(), name='author-contact'),
                       url(r'^(?P<pk>\d+)/$', AuthorProfile.as_view(), name='author-profile'),)