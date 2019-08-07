from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from photogur.forms import LoginForm

from photogur.forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/pictures')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/pictures')   


@login_required
def function_name(request):
    pass


def root(request):
    return HttpResponseRedirect('pictures')

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
    search_results = Picture.objects.filter(artist__contains=query) or Picture.objects.filter(title__contains=query) or Picture.objects.filter(url__contains=query)
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


