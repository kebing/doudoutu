# Create your views here.

from django.shortcuts import render_to_response

from tuan.models import models

def tuan(request):
    """
    """

    deals = models.Deal.objects.all()
    

    return render_to_response('tuan.html', {'deals' : deals})



