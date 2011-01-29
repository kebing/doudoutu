from django.conf.urls.defaults import *

import views

urlpatterns = patterns(
    '',
    (r'^city/(?P<city>[a-zA-Z]+)/$', views.tuan_city),
    (r'^category/(?P<category>\w+)/$', views.tuan_category),
    (r'^$', views.tuan),
    
    
)
