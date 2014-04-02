from django.conf.urls import patterns, include, url
from meetups.views import *



urlpatterns = patterns('',
    url(r'^active$', MeetupView.as_view(), name='meetup'),
    url(r'^register$', RegisterView.as_view(), name='register'),
)