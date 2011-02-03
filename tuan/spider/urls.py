from django.conf.urls.defaults import *

import views

urlpatterns = patterns(
    '',
    (r'^default/', views.load_default_site_data),
    (r'^deal/', views.deal_spider),
    #(r'^city/', views.city_spider),

)
