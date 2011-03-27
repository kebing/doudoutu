# -*-coding:utf-8-*-

import models
import ip_convert
from django.shortcuts import render_to_response
import jsonlib as json
import logging
from ip469 import settings
import socket

logging.basicConfig(filename=settings.LOG_ROOT + 'ip_views.log', level=logging.DEBUG)

COOKIE_QUERY_HISTORY = 'qh'
MAX_QUERY_HISTORY=10

def uniq(query_history):
    tmp_key=[]
    uniq_history=[]
    for k,v in query_history:
        if not k in tmp_key:
            tmp_key.append(k)
            uniq_history.append([k,v])
    return uniq_history

def get_client_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']

def query_by_ipv4_inner(request, ipv4):
    """
    """
    logger = logging.getLogger('query_by_ipv4_inner')
    ip_infos = models.Ipv4Info.objects.filter_by_ip(ipv4)
    ip_string = ip_convert.ipv4_to_string(ipv4)
    ip_value = ip_convert.ipv4_int2readable(ipv4)
    ip_client_string = get_client_ip(request)
    ip_client_value = ip_convert.ipv4_from_string(ip_client_string)
    logger.debug('from ' + ip_client_string + ' query ' + ip_string + ' return ' + str(ip_infos.count()) + ' results')
    new_query_history = []
    if ip_infos.count() > 0:
        new_query_history.append([ip_string, unicode(ip_infos[0])])
    if COOKIE_QUERY_HISTORY in request.COOKIES:
        old_query_history = request.COOKIES[COOKIE_QUERY_HISTORY]
        try:
            old_query_history = json.loads(old_query_history)
        except json.ReadError:
            old_query_history = []
        old_query_history = uniq(old_query_history)
        new_query_history.extend(old_query_history)
        new_query_history = uniq(new_query_history)[:MAX_QUERY_HISTORY]
    response = render_to_response('ipinfo.html', locals())
    try:
        new_query_history_str = json.dumps(new_query_history)
        response.set_cookie(key=COOKIE_QUERY_HISTORY,
                            value=new_query_history_str, 
                            max_age=86400,
                            expires=None,
                            path='/',
                            domain=None,
                            secure=None)
    except json.WriteError:
        response.delete_cookie(key=COOKIE_QUERY_HISTORY)
        print 'write error: '
        print new_query_history
    except json.UnknownSerializerError:
        response.delete_cookie(key=COOKIE_QUERY_HISTORY)
        print 'error'
    return response


def query_by_ipv4(request, ipv4):
    """
    """
    ipv4_inner = ip_convert.ipv4_readable2int(ipv4)
    return query_by_ipv4_inner(request, ipv4_inner)

def query_by_ipv4_string(request, ipv4_string):
    """
    """
    ipv4 = ip_convert.ipv4_from_string(ipv4_string)
    return query_by_ipv4(request, ipv4)


def query_by_domain(request, domain):
    """
    """
    ip = socket.gethostbyname(domain)
    return query_by_ipv4_string(request, ip)


def query_by_ipv6_inner(request, ipv6):
    """
    """
    #no_ip_info = True
    ip_string = ip_convert.ipv6_to_string(ipv6)
    ip_value = ip_convert.ipv6_tuple2readable(ipv6)
    return render_to_response('ipinfo.html', locals())

def query_by_ipv6(request, ipv6):
    """
    """
    ipv6_inner = ipv6_readable2tuple(ipv6)
    return query_by_ipv6_inner(request, ipv6_inner)

def query_by_ipv6_string(request, ipv6_string):
    """
    """
    return query_by_ipv6(request, ipv6)

def default(request):
    """
    """
    logger = logging.getLogger('default')
    ip_client_string = get_client_ip(request)
    ip_client_value = ip_convert.ipv4_from_string(ip_client_string)
    logger.debug('from ' + ip_client_string)
    if COOKIE_QUERY_HISTORY in request.COOKIES:
        new_query_history = request.COOKIES[COOKIE_QUERY_HISTORY]
        try:
            new_query_history = json.loads(new_query_history)
        except json.ReadError:
            new_query_history = []
    return render_to_response('ipinfo.html', locals())
