# -*-coding:utf-8-*-

from spider_base import *
from tuan.models import models

class DealSpider:
    def fetch_and_parse(self, spider, url):
        usock = urllib.urlopen(url)
        data = usock.read()
        usock.close()
        spider.feed(data)
        spider.close()
    
    def store_result(self, spider, site, city):
        grabtime = datetime.datetime.now();
        n = 0
        for url, value, price, title, image, timeleft in spider.zip_info():
            query=models.Deal.objects.filter(url__iexact=url).filter(city=city)
            if query.count() <= 0:
                deal = models.Deal()
                deal.url = url
                deal.value = float(value)
                deal.price = float(price)
                deal.rebate = deal.price / deal.value
                deal.saving = deal.value - deal.price
                deal.title = title
                deal.image = image
                deal.timeleft = timeleft
                deal.grabtime = grabtime
                deal.site = site
                deal.categorie = 0;
                deal.city = city;
                deal.save()
                n += 1
        return n
                

            

class CitySpider:
    def fetch_and_parse(self, spider, url):
        usock = urllib.urlopen(url)
        data = usock.read()
        usock.close()
        spider.feed(data)
        spider.close()
    
    def store_result(self, spider, site):
        grabtime = datetime.datetime.now();
        n = 0
        for city, name, url in spider.zip_info():
            # 城市补全
            query = models.City.objects.filter(city=city)
            if query.count() <= 0:
                models.City(city=city, name=name).save()
            # 对应关系存储
            query = models.SiteCity.objects.filter(site=site, city=city)
            if query.count() <= 0:
                sc = models.SiteCity()
                sc.site = site
                sc.city = city
                sc.name = name
                sc.url = url
                sc.grabtime = grabtime
                sc.save()
                n+=1
        return n
            
    
    
