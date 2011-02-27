from django.conf.urls.defaults import *

urlpatterns = patterns(
    'ip469.tuan.views',
    (r'^$', 'tuan'),
    (r'^(?P<page>\d+)/$', 'tuan_page'),
    (r'^(?P<city>[a-zA-Z\-_]+)/$', 'tuan_city'),
    (r'^(?P<city>[a-zA-Z\-_]+)/page/(?P<page>\d+)/$', 'tuan_city_page'),
    (r'^(?P<city>[a-zA-Z\-_]+)/category/(?P<category>\d+)/$', 'tuan_city_category'),
    (r'^(?P<city>[a-zA-Z\-_]+)/category/(?P<category>\d+)/page/(?P<page>\d+)/$', 'tuan_city_category_page'),
)
