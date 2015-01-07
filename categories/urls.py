from django.conf.urls import patterns, url, include
from categories.views import categories


urlpatterns = patterns('categories.views',
    url(r'^$', categories, {}, name='categories'),
)