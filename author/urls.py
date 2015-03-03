from django.conf.urls import patterns, url
from author.views import ContactFormView, RegistrationFormView

__author__ = 'k1'

urlpatterns = patterns('',
                       url(r'^registration/$', RegistrationFormView.as_view(), name='author-register'),
                       url(r'^contact/$', ContactFormView.as_view(), name='author-contact'), )