# Create your views here.

from django.shortcuts import render_to_response

from tuan.models import models

def tuan(request):
    """
    """

    deals = models.Deal.objects.all()
    

    return render_to_response('tuan.html', {'deals' : deals})





def tuan_city(request, city):
    """
    """

    print city
    deals = models.Deal.objects.filter(city=city)
    
    return render_to_response('tuan.html', {'deals' : deals})


def tuan_categorie(request, categorie):
    """
    """

    deals = models.Deal.objects.all()
    

    return render_to_response('tuan.html', {'deals' : deals})

