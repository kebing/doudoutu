# -*-coding:utf-8-*-

from django.shortcuts import render_to_response
from django.template import Context, loader, Template
from django.http import HttpResponse

from tuan.models import models
from tuan.spider.spider_all import SpiderFactory
from tuan.spider.spider import DealSpider
from tuan.spider.spider import CitySpider

def deal_spider(request):
    """
    """

    response = HttpResponse()
    response['Cache-Control'] = 'no-cache'

    html_header = loader.get_template('header.html').render(Context())
    html_footer = loader.get_template('footer.html').render(Context())

    tpl_fetch = Template('<p>Fetching from {{site}} @ {{city}} : {{url}} ... ')
    tpl_store = Template('{{n}} deals.</p>')
    tpl_total = Template('<p>总共抓取 {{total}} 条记录</p>')

    response.write(html_header)

    query=models.SiteCity.objects.all()
    total = 0
    for sc in query:
        factory=SpiderFactory()
        engine = DealSpider()
        spider = factory.new_deal_spider(sc.site)
        engine.fetch_and_parse(spider, sc.url)
        response.write(tpl_fetch.render(Context({'url': sc.url, 'site':sc.site, 'city':sc.city})));
        n = engine.store_result(spider, sc.site, sc.city)
        response.write(tpl_store.render(Context({'n': n})))
        total += n
    response.write(tpl_total.render(Context({'total':total})))

    response.write(html_footer)

    return response


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
