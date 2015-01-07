from django.conf.urls import patterns, url
from discussions.views import categories, post_topic


urlpatterns = patterns('categories.views',

    url(r'^$', categories, {}, name='categories'),

)