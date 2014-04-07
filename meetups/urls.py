from django.conf.urls import patterns, include, url
from meetups.views import *



urlpatterns = patterns('',
    url(r'^(?P<meetup_id>\d+)$', MeetupView.as_view(), name='meetup'),
)