# -*-coding:utf-8-*-

from django.db import models
from django.contrib import admin
from django.utils import encoding

class Ipv4InfoManager(models.Manager):
    def filter_by_ip(self, ipv4):
        return super(Ipv4InfoManager, self).get_query_set().\
            filter(start_ip__lte=ipv4, end_ip__gte=ipv4).order_by('-city')[:5]


class Ipv4Info(models.Model):
    start_ip = models.BigIntegerField()
    end_ip = models.BigIntegerField()
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    isp = models.CharField(max_length=255)
    objects = Ipv4InfoManager()
    def __unicode__(self):
        return self.province.decode('utf8') + ' ' + self.city.decode('utf8') + ' ' + self.isp.decode('utf8')
    #def __str__(self):
    #    return encoding.iri_to_uri(unicode(self))


admin.site.register(Ipv4Info)
