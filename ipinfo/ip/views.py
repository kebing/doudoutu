
import models
import ip_convert
from django.shortcuts import render_to_response


def query_by_ipv4_inner(request, ipv4):
    """
    """
    ip_infos = models.Ipv4Info.objects.filter_by_ip(ipv4)
    #no_ip_info = True
    #for info in ip_infos:
    #    no_ip_info = False
    #    print info.province
        #info.province = info.province.encode('utf-8')
        #info.city = info.city.encode('utf-8')
        #info.isp = info.isp.encode('utf-8')
    ip_string = ip_convert.ipv4_to_string(ipv4)
    ip_value = ip_convert.ipv4_int2readable(ipv4)
    return render_to_response('ipinfo.html', locals())

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
