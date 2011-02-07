# -*-coding:utf-8-*-

import datetime

from django.shortcuts import render_to_response
from django.template import Context, loader, Template
from django.http import HttpResponse

from tuan.models import models
from tuan.spider.spider_all import SpiderFactory
from tuan.spider.spider import DealSpider
from tuan.spider.spider import CitySpider
import site_data

def deal_spider_site_city(request, site, city):
    """
    """

    response = HttpResponse()
    response['Cache-Control'] = 'no-cache'

    html_header = loader.get_template('header.html').render(Context())
    html_footer = loader.get_template('footer.html').render(Context())

    tpl_fetch = Template('<p>Fetching from {{site}} @ {{city}} : {{url}} ... ')
    tpl_store = Template('{{n}} deals.</p>')
    tpl_fetch_fail = Template(' fail.</p>')
    tpl_total = Template('<p>总共抓取 {{total}} 条记录</p>')

    response.write(html_header)

    query=None
    if (site != None) and (city != None):
        query = models.SiteCity.objects.filter(site=site, city=city)
    elif (site != None) and (city is None):
        query = models.SiteCity.objects.filter(site=site)
    elif (site is None) and (city != None):
        query = models.SiteCity.objects.filter(city=city)
    else:
        query = models.SiteCity.objects.all()
    total = 0
    for sc in query:
        factory=SpiderFactory()
        engine = DealSpider()
        spider = factory.new_deal_spider(sc.site)
        response.write(tpl_fetch.render(Context({'url': sc.url, 'site':sc.site, 'city':sc.city})));
        ok = engine.fetch_and_parse(spider, sc.url)
        if ok:
            n = engine.store_result(spider, sc.site, sc.city)
            response.write(tpl_store.render(Context({'n': n})))
            total += n
        else:
            response.write(tpl_fetch_fail.render(Context({})))
    response.write(tpl_total.render(Context({'total':total})))

    response.write(html_footer)

    return response

def deal_spider_site(request, site):
    return deal_spider_site_city(request, site, None)

def deal_spider_city(request, city):
    return deal_spider_site_city(request, None, city)

def deal_spider_all(request):
    return deal_spider_site_city(request, None, None)

def city_spider(request):
    response = HttpResponse()
    response['Cache-Control'] = 'no-cache'

    html_header = loader.get_template('header.html').render(Context())
    html_footer = loader.get_template('footer.html').render(Context())

    tpl_fetch = Template('<p>Fetching from {{site}} : {{url}} ... ')
    tpl_store = Template('{{n}} cities.</p>')
    tpl_total = Template('<p>总共抓取 {{total}} 条记录</p>')

    response.write(html_header)

    query=models.Site.objects.all()
    total=0
    for site in query:
        factory=SpiderFactory()
        engine = CitySpider()
        spider = factory.new_city_spider(site.site)
        engine.fetch_and_parse(spider, site.url)
        response.write(tpl_fetch.render(Context({'url':site.url, 'site':site.site})))
        n=engine.store_result(spider, site.site)
        response.write(tpl_store.render(Context({'n':n})))
        total += n
        print n
    response.write(tpl_total.render(Context({'total':total})))
    print total

    response.write(html_footer)

    return response


def load_default_site_data(request):
    '''从site_data.py加载默认网站数据'''
    response = HttpResponse()
    
    html_header = loader.get_template('header.html').render(Context())
    html_footer = loader.get_template('footer.html').render(Context())

    tpl_exists = Template('[WARN] {{model_name}} {{key}} <strong>already exists</strong>: {{detail}}<br/>')
    tpl_ok = Template('[INFO] {{model_name}} {{key}} <strong>saved</strong><br/>')
    tpl_multi = Template('<strong>[ERROR]</strong> Multi {{key}} in model {{model_name}} exists<br/>')

    response.write(html_header)

    model_name='City'
    for key,v in site_data.city_list.iteritems():
        try:
            city = models.City.objects.get(city=key)
            detail = city.name + ' ' + str(city.rank)
            response.write(tpl_exists.render(Context(locals())))
        except models.City.DoesNotExist:
            city = models.City(city=key, name=v[0], rank=v[1])
            city.save()
            response.write(tpl_ok.render(Context(locals())))
        except models.City.MultipleObjectsReturned:
            response.write(tpl_multi.render(Context(locals())))
    model_name='Site'
    for key,v in site_data.site_list.iteritems():
        try:
            site = models.Site.objects.get(site=key)
            detail = site.name + ' ' + site.url + ' ' + str(site.rank)
            response.write(tpl_exists.render(Context(locals())))
        except models.Site.DoesNotExist:
            site = models.Site(site=key, name=v[0], url=v[1], rank=v[2])
            site.save()
            response.write(tpl_ok.render(Context(locals())))
        except models.Site.MultipleObjectsReturned:
            response.write(tpl_multi.render(Context(locals())))
    model_name='SiteCity'
    for key,v in site_data.site_city_list.iteritems():
        try:
            site_city = models.SiteCity.objects.get(site=v[0], city=v[1])
            detail = site_city.name + ' ' + site_city.url + ' ' + str(site_city.grabtime)
            response.write(tpl_exists.render(Context(locals())))
        except models.SiteCity.DoesNotExist:
            site_city = models.SiteCity(site=v[0], city=v[1],
                                        name=v[2], url=v[3], grabtime=datetime.datetime.now())
            site_city.save()
            response.write(tpl_ok.render(Context(locals())))
        except models.SiteCity.MultipleObjectsReturned:
            response.write(tpl_multi.render(Context(locals())))
    response.write(html_footer)
    return response

