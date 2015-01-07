from django.conf.urls import patterns, include, url
from django.contrib import admin
from discussions.views import category, topic, post_topic, addcomment
from institutions.views import InstitutionList
from listings.views import add, post
from netisell import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'netisell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^(?P<abbr>[\w-]+)/discussions/post_topic$', post_topic, {}, name='post_topic'),
    url(r'^(?P<abbr>[\w-]+)/discussion/comment', addcomment, {}, name=addcomment),
    url(r'^(?P<abbr>[\w-]+)/topic/(?P<topic_id>[\w-]+)/(?P<topic_slug>[\w-]+)', topic, {}, name=topic),
    url(r'^(?P<abbr>[\w-]+)/(?P<section_slug>[\w-]+)/(?P<post_id>\d+)/(?P<post_slug>[\w-]+)$', post, {}, name='post'),
    url(r'^(?P<abbr>[\w-]+)/discussions', include('discussions.urls')),
    url(r'^(?P<abbr>[\w-]+)/discussions/(?P<discussion_category>[\w-]+)', category, {}, name=category),
    url(r'^add$', add, {}, name='add'),
    url(r'^', include('institutions.urls')),
    url(r'^', include('discussions.urls')),
    url(r'^(?P<abbr>[\w-]+)/(?P<section_slug>[\w-]+)$', include('categories.urls')),
    url(r'^(?P<abbr>[\w-]+)/(?P<section_slug>[\w-]+)/(?P<category_slug>[\w-]+)$', include('listings.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT,
}),
)