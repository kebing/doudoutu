# -*-coding:utf-8-*-

import datetime
from django.shortcuts import render_to_response

import models

DEFAULT_COUNT_PER_PAGE = 30
PAGE_BAD = 0
PAGE_1ST = 1
DEFAULT_PAGE = PAGE_1ST
CATEGORY_ALL = 0
DEFAULT_CATEGORY = CATEGORY_ALL
MAX_TITLE_LEN = 75

def tuan_city_category_page(request, city, category, page):
    """
    """
    try:
        category = int(category)
    except ValueError:
        category = DEFAULT_CATEGORY
        
    try:
        page = int(page)
    except ValueError:
        page = DEFAULT_CATEGORY
    if page < PAGE_1ST: page = PAGE_1ST
    count = DEFAULT_COUNT_PER_PAGE
    deals = None
    if category == 0:
        deals = models.Deal.objects.filter(city=city)
    else:
        deals = models.Deal.objects.filter(city=city, category=category)
    deals = deals.filter(time_end__gte=datetime.datetime.now()).order_by('-rank')
    total = deals.count()
    if total != 0:
        deals = deals[ (page - 1) * count : (page - 1) * count + count]
    max_page = (total / count) + ( (total % count > 0) and 1 or 0 )
    next_page = (page < max_page) and page + 1 or PAGE_BAD
    prev_page = (page > PAGE_1ST) and (page - 1) or PAGE_BAD
    for deal in deals:
        if len(deal.title) <= MAX_TITLE_LEN:
            deal.title_short = deal.title
        else:
            deal.title_short = deal.title[:MAX_TITLE_LEN] + unicode('…','utf-8') #'...'
        site = models.Site.objects.filter(site=deal.site)
        if site.count() == 1:
            deal.site_name = site[0].name
            site_city = models.SiteCity.objects.filter(site=deal.site,city=deal.city)
            if site_city.count() == 1:
                deal.site_url = site_city[0].url
            else:
                deal.site_url = site[0].url
        else:
            deal.site_name = ''
    # 获取城市名称
    city_name = city
    city_query = models.City.objects.filter(city=city)
    if city_query.count() == 1:
        city_name = city_query[0].name
    # 获取团购网站列表
    site = models.Site.objects.all()
    return render_to_response('tuan.html', locals())

def tuan_city_category(request, city, category):
    return tuan_city_category_page(request, city, category, DEFAULT_PAGE)

def tuan_city_page(request, city, page):
    return tuan_city_category_page(request, city, DEFAULT_CATEGORY, page)

def tuan_city(request, city):
    return tuan_city_page(request, city, DEFAULT_PAGE)

def tuan_page(request, page):
    return tuan_city_page(request, 'shenzhen', page)

def tuan(request):
   return tuan_page(request, DEFAULT_PAGE)


