from django.conf.urls import patterns, url
from account.views import DashboardView, AccountRegistrationView, LoginView, LogoutView, PasswordRecoveryView, \
    SettingsView

__author__ = 'k1'

urlpatterns = patterns('',
                       # this urls added for Go Django tutorial
                       url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
                       url(r'^register/$', AccountRegistrationView.as_view(), name='register'),
                       url(r'^login/$', LoginView.as_view(), name='login'),
                       url(r'^logout/$', LogoutView.as_view(), name='logout'),
                       url(r'^password_recovery/$', PasswordRecoveryView.as_view(), name='password_recovery'),
                       url(r'^settings/$', SettingsView.as_view(), name='settings')
                       ,)