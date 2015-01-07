from django.conf.urls import patterns, url, include
from institutions.views import InstitutionList


urlpatterns = patterns('institutions.views',
    url(r'^$', InstitutionList.as_view(), name='home'),
    url(r'^(?P<abbr>[\w-]+)/$', include('sections.urls')),
)