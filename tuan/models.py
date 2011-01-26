# -*-coding:gb18030-*-

from django.db import models


# 团购商品的信息
class Deal(models.Model):
    url = models.CharField(max_length=1024) # 商品URL
    value = models.FloatField()             # 原价
    price = models.FloatField()             # 现价
    rebate = models.FloatField()            # 折扣
    title = models.CharField(max_length=1024) # 标题
    image = models.CharField(max_length=1024) # 图片URL
    uptime = models.DateTimeField(auto_now=True) # 商品上架时间
    downtime = models.DateTimeField(auto_now=True) # 商品下架时间
    #bought = models.IntegerField()             # 已购买人数
    site = models.IntegerField()              # 所属团购网站ID
    categorie = models.IntegerField()         # 商品分类
    city = models.IntegerField()              # 城市
    
    def __unicode__(self):
        return self.title

    class Admin:
        pass
    

# 团购网站的信息
class Site(models.Model):
    name = models.CharField(max_length=1024) # 网站名称
    url = models.CharField(max_length=1024)  # 网站URL
    
    def __unicode__(self):
        return self.name

    class Admin:
        pass

# 商品分类
class Categorie(models.Model):
    name = models.CharField(max_length=64) # 分类名称
    
    def __unicode__(self):
        return self.name

# 城市信息
class City(models.Model):
    name = models.CharField(max_length=64) # 城市名称
    
    def __unicode__(self):
        return self.name
    
    class Admin:
        pass
    

# 团购网站和城市的对应关系
class SiteCityMap(models.Model):
    site = models.IntegerField()
    city = models.IntegerField()
    url = models.CharField(max_length=1024) # 团购网站子城市URL
    
    def __unicode__(self):
        return self.site + '-' + self.city
    
    class Admin:
        pass
