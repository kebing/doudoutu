from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^deal/', views.deal_spider),
    (r'^city/', views.city_spider),

)
