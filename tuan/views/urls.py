from django.conf.urls.defaults import *

import views

urlpatterns = patterns(
    '',
    (r'^city/(?P<city>[a-zA-Z]+)/$', views.tuan_city),
    (r'^categorie/(?P<categorie>\w+)/$', views.tuan_categorie),
    (r'^$', views.tuan),
    
    
)
