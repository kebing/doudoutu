# -*-coding:utf-8-*-

import logging
from spider_base import *
from tuan.models import models

class DealSpider:
    logger = logging.getLogger('tuan.spider.DealSpider')
    def fetch_and_parse(self, spider, url):
        return fetch_and_parse(spider, url)
    def store_result(self, spider, site, city):
        grabtime = datetime.datetime.now();
        n = 0
        site_rank = 0
        try:
            query_site = models.Site.objects.get(site=site)
            site_rank = query_site.rank
        except models.Site.DoesNotExist:
            # 出错，网站信息不存在！
            self.logger.error('site <' + site + '> info not exists')
        except models.Site.MultipleObjectsReturned:
            # 出错，网站信息多于一个！
            self.logger.error('site <' + site + '> info has multi records')
        for url, value, price, title, image, time_end, bought in spider.zip_info():
            query=models.Deal.objects.filter(url__iexact=url).filter(city=city)
            if query.count() <= 0:
                deal = models.Deal()
                deal.url = url
                deal.value = float(value)
                deal.price = float(price)
                if deal.value <= 0:
                    deal.rebate = 0
                else:
                    #deal.rebate = float("{0:.1f}".format(deal.price * 10 / deal.value))
                    deal.rebate = float("%(0).1f" % {'0':deal.price * 10 / deal.value})
                deal.saving = deal.value - deal.price
                deal.title = title
                deal.image = image
                deal.time_end = time_end
                deal.grabtime = grabtime
                deal.updatetime = grabtime
                deal.bought = float(bought)
                deal.site = site
                deal.city = city
                deal.category = 0
                deal.rank = site_rank
                deal.save()
                n += 1
                self.logger.debug('deal saved, site=' + site + ',city=' + city + ',url=' + url)
            elif query.count() == 1:
                # 更新
                deal = query[0]
                deal.value = float(value)
                deal.price = float(price)
                if deal.value <= 0:
                    deal.rebate = 0
                else:
                    #deal.rebate = float("{0:.1f}".format(deal.price * 10 / deal.value))
                    deal.rebate = float("%(0).1f" % {'0':deal.price * 10 / deal.value})
                deal.saving = deal.value - deal.price
                deal.title = title
                deal.image = image
                deal.time_end = time_end
                deal.updatetime = grabtime
                deal.bought = float(bought)
                if deal.rank < site_rank:
                    deal.rank = site_rank
                deal.save()
                n += 1
                self.logger.debug('deal updated, site=' + site + ',city=' + city + ',url=' + url)
            else:
                # 错误！
                self.logger.error('multi deals exist, site=' + site + ',city=' + city + ',url=' + url)
        return n
                

            

class CitySpider:
    def fetch_and_parse(self, spider, url):
        return fetch_and_parse(spider, url)
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
            
    
    
