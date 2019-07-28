from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import *

def pictures_view(request):



    context = { 
        'pictures': Picture.objects.all(),
        'comments': Comment.objects.all(),
    }


    response = render(request, 'pictures.html', context)
    return HttpResponse(response)