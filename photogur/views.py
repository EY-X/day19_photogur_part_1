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

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}

    response = render(request, 'picture.html', context)
    return HttpResponse(response)

def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}

    response = render(request, 'search.html', context)
    return HttpResponse(response)



