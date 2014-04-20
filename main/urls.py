from django.conf.urls import patterns, include, url

# View
from main.views import IndexView, AboutView, ContactView, ArchiveView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^archive$', ArchiveView.as_view(), name='archive'),
)

# Apps
urlpatterns += patterns('',
    url(r'^meetups/', include('meetups.urls')),
)
