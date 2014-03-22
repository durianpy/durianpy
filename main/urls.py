from django.conf.urls import patterns, include, url

# View
from main.views import *


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
)