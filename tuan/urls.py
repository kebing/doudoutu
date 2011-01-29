# -*-coding:gb18030-*-
from django.conf.urls.defaults import *

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Example:
    # (r'^tuan/', include('tuan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

    (r'^spider/', include('tuan.spider.urls')),
)

urlpatterns += patterns(
    'views.views',
    # <city>/category/<category>/page/<page>/
    (r'^$', 'tuan'),
    (r'^(?P<page>\d+)/$', 'tuan_page'),
    (r'^(?P<city>[a-zA-Z\-_]+)/$', 'tuan_city'),
    (r'^(?P<city>[a-zA-Z\-_]+)/page/(?P<page>\d+)/$', 'tuan_city_page'),
    (r'^(?P<city>[a-zA-Z\-_]+)/category/(?P<category>\d+)/$', 'tuan_city_category'),
    (r'^(?P<city>[a-zA-Z\-_]+)/category/(?P<category>\d+)/page/(?P<page>\d+)/$', 'tuan_city_category_page'),
)
