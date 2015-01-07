from django.conf.urls import patterns, url, include
from sections.views import sections


urlpatterns = patterns('sections.views',
    url(r'^$', sections, {}, name='sections'),
)