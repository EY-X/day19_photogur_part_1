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

def create_comment(request):
    picture = request.POST['picture']
    picture_id = Picture.objects.get(pk=picture)
    name = request.POST['name_comment_name']
    message = request.POST['message_comment_name']
    new_comment = Comment(name=name, message=message, picture=picture_id)
    new_comment.save()
    context = {'picture': picture_id}
    return render(request,'picture.html', context)
    # return HttpResponseRedirect(f'/pictures/{picture}')


