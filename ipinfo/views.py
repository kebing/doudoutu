
import ip.ip_convert
from django.shortcuts import render_to_response


def index(request):
    """
    """
    ip_string = request.META['REMOTE_ADDR']
    ip_value = ip.ip_convert.ipv4_from_string(ip_string)
    return render_to_response('index.html', locals())
