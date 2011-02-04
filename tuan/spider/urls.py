from django.conf.urls.defaults import *

import views

urlpatterns = patterns(
    '',
    (r'^default/', views.load_default_site_data),
    
    (r'^deal/$', views.deal_spider_all),
    (r'^deal/site/(?P<site>[a-zA-Z\-_]+)/$', views.deal_spider_site),
    (r'^deal/city/(?P<city>[a-zA-Z\-_]+)/$', views.deal_spider_city),
    (r'^deal/site/(?P<site>[a-zA-Z-_]+)/city/(?P<city>[a-zA-Z-_]+)/$', views.deal_spider_site_city),
    #(r'^city/', views.city_spider),

)
