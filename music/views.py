from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django.http import HttpResponseRedirect
#from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return  Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')



def user_login(request):
    context = {}
    if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(username=username, password=password) 
       if user:
            login(request, user)
            return HttpResponseRedirect(reverse('music:index'))
       else:
            return render(request, 'music/login.html')
    else:
        return render(request, 'music/login.html')



def user_logout(request):
    logout(request)
    #return render(request, 'music/index.html')
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums' : all_albums})


def user_success(request):
    return render(request, 'music/success.html')

