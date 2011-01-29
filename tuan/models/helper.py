# -*-coding:utf-8-*-

import django.db.models.Q
import models

class DealHelper:
    start = 0
    count = 30
    city = None
    category = None

def query_deal(city = None, category = None, start = 0, count = 30):
    query = None
    if city is None and category is None:
    fffffdfffff    return models.Deal.objects.all()[start:count]
    elif city != None and category is None:
        return models.Deal.objects.filter(city=city)[start:count]
    elif city i



s None and category != None:
        return models.Deal.objects.filter(category=category)[start:count]
    else:                   # all not None
        return models.Deal.objects.filter(city=city, category=category)[start:count]
