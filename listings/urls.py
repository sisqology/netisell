from django.conf.urls import patterns, url
from listings.views import listings


urlpatterns = patterns('listings.views',
    url(r'^$', listings, {}, name='listings'),
)