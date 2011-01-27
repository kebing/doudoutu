# -*-coding:gb18030-*-

from django.db import models
from django.contrib import admin


# �Ź���Ʒ����Ϣ
class Deal(models.Model):
    url = models.CharField(max_length=1024) # ��ƷURL
    value = models.FloatField()             # ԭ��
    price = models.FloatField()             # �ּ�
    rebate = models.FloatField()            # �ۿ�
    saving = models.FloatField()
    title = models.CharField(max_length=1024) # ����
    image = models.CharField(max_length=1024) # ͼƬURL
    uptime = models.DateTimeField(auto_now=True) # ��Ʒ�ϼ�ʱ��
    downtime = models.DateTimeField(auto_now=True) # ��Ʒ�¼�ʱ��
    #bought = models.IntegerField()             # �ѹ�������
    site = models.IntegerField()              # �����Ź���վID
    categorie = models.IntegerField()         # ��Ʒ����
    city = models.IntegerField()              # ����
    
    def __unicode__(self):
        return self.title

    class Admin(admin.ModelAdmin):
        pass
    

# �Ź���վ����Ϣ
class Site(models.Model):
    name = models.CharField(max_length=1024) # ��վ����
    url = models.CharField(max_length=1024)  # ��վURL
    
    def __unicode__(self):
        return self.name


# ��Ʒ����
class Categorie(models.Model):
    name = models.CharField(max_length=64) # ��������
    
    def __unicode__(self):
        return self.name

# ������Ϣ
class City(models.Model):
    name = models.CharField(max_length=64) # ��������
    
    def __unicode__(self):
        return self.name
    

    

# �Ź���վ�ͳ��еĶ�Ӧ��ϵ
class SiteCityMap(models.Model):
    site = models.IntegerField()
    city = models.IntegerField()
    url = models.CharField(max_length=1024) # �Ź���վ�ӳ���URL
    
    def __unicode__(self):
        return self.site + '-' + self.city
    

admin.site.register(Deal, Deal.Admin)
admin.site.register(Site)
admin.site.register(Categorie)
admin.site.register(City)
admin.site.register(SiteCityMap)
