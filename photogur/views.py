from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from photogur.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from photogur.forms import LoginForm, PictureForm

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('pictures')
    else:
        form = UserCreationForm()
    html_response =  render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)




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


@login_required
def picture_new(request):
    return render(request, 'picture-form.html',{
        'form': PictureForm(),
        'message': 'Post a picture!!',
        'action': '/pictures/create'
    })


@login_required
def picture_create(request):
    form = PictureForm(request.POST)
    if form.is_valid():
        new_pic = form.save(commit=False)
        new_pic.user = request.user

        new_pic.save()
    return HttpResponseRedirect('/pictures')

@login_required
def edit_picture(request, id):
    picture = get_object_or_404(Picture, pk=id, user=request.user.pk)
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            artist = form.cleaned_data.get('artist')
            url = form.cleaned_data.get('url')
            picture.title = title
            picture.artist = artist
            picture.url = url
            picture.save()
            return HttpResponseRedirect('/pictures')
    form = PictureForm(request.POST)
    context = {'picture': picture, 'form': form}
    return HttpResponse(render(request, 'edit.html', context))


picture = get_object_or_404(Picture, pk=<PICTURE ID GOES HERE>, user=request.user.pk)
# code to render edit template as usual