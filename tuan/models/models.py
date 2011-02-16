# -*-coding:utf-8-*-

from django.db import models
from django.contrib import admin


# 团购商品的信息
class Deal(models.Model):
    url = models.TextField() # 商品URL
    value = models.FloatField()             # 原价
    price = models.FloatField()             # 现价
    rebate = models.FloatField()            # 折扣
    saving = models.FloatField()
    title = models.TextField() # 标题
    image = models.TextField() # 图片URL
    time_end = models.DateTimeField(help_text='商品结束时间')
    grabtime = models.DateTimeField(help_text='信息抓取时间')
    updatetime = models.DateTimeField(help_text='信息更新时间')
    bought = models.IntegerField(default=0, help_text='已购买人数')
    site = models.CharField(max_length=64, help_text='所属团购网站')
    city = models.CharField(max_length=64, help_text='城市')
    category = models.IntegerField(default=0, help_text='商品分类')
    rank = models.IntegerField(default=0, help_text='商品等级')
    def __unicode__(self):
        return self.title
    class Admin(admin.ModelAdmin):
        pass


# 团购网站的信息
class Site(models.Model):
    site = models.CharField(primary_key=True, max_length=64) # 网站
    name = models.CharField(max_length=64) # 网站名称
    url = models.TextField()  # 网站URL
    rank = models.IntegerField(default=0, help_text='网站等级')
    def __unicode__(self):
        return self.name


# 商品分类
class Category(models.Model):
    name = models.CharField(max_length=64) # 分类名称
    rank = models.IntegerField(default=0, help_text='分类等级')
    def __unicode__(self):
        return self.name


# 城市信息
class City(models.Model):
    city = models.CharField(primary_key=True, max_length=64) # 城市
    name = models.CharField(max_length=64) # 城市名称
    rank = models.IntegerField(default=0, help_text='城市等级')
    def __unicode__(self):
        return self.name

    

# 各城市网站
class SiteCity(models.Model):
    site = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    url = models.TextField() # 团购网站子城市URL
    grabtime = models.DateTimeField(help_text='抓取时间')
    def __unicode__(self):
        return self.name
    

admin.site.register(Deal, Deal.Admin)
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(SiteCity)
