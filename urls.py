from django.conf.urls import patterns, include, url
from django.contrib import admin
from institutions.views import InstitutionList
from lists.views import listing

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', InstitutionList.as_view(), name='home'),
    url(r'^', include('categories.urls')),
    url(r'^(?P<alias>[\w-]+)/(?P<category>[\w-]+)/(?P<subcategory>[\w-]+)$', include('lists.urls')),
    #url(r'^listing/', include('lists.urls')),
    url(r'^listing/(?P<listing_id>\d+)/(?P<listing_slug>[\w-]+)$', listing, {}, name='listing'),
    # url(r'^blog/', include('blog.urls')),
)
