from django.conf.urls.defaults import *

urlpatterns = patterns(
    'ip469.ip.views',
    (r'^(?P<ipv4>[0-9]+)/', 'query_by_ipv4'),
    (r'^(?P<ipv4_string>[0-9.]+)/', 'query_by_ipv4_string'),
    (r'^(?P<ipv6_string>[0-9a-zA-Z:]+)/', 'query_by_ipv6_string'),
    (r'^(?P<domain>[0-9a-zA-Z_\-.]+)/', 'query_by_domain'),
    (r'^$', 'default'),
)
