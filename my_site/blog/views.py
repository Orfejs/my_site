import json
import os.path
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView
    )
import requests
from requests.api import get
from requests.models import parse_url
from .models import Post
from .models import ApiCall
from .forms import ApiCallForm


# def home(request):
    
#     form = ApiCallForm()
    
#     if request.method == 'POST':
#         print(request.POST)
#         form = ApiCallForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     # context = {
#     #     'posts': Post.objects.all()
#     # }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class ApiCallView(DetailView):
    model = ApiCall
    template_name = 'blog/link.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'apicalls'
    ordering = ['-date_posted']
    


def about(request):
    response = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
    picture = response.json()
    my_picture = picture[0]
    random_pic = my_picture['urls']
    return render(request, 'blog/about.html', {
        'img': random_pic['regular']
        
        
        
    })

def create_view(request):
    response = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
    picture = response.json()
    my_picture = picture[0]
    random_pic = my_picture['urls']
    reg_pic = random_pic['regular']
    b = ApiCall(name = reg_pic)
    b.save()
    return render(request, 'blog/create.html')


def link_view(request):
    context = {
        'apicalls': ApiCall.objects.all()
    }
    return render(request, 'blog/link.html', context)
#     # context = {
#     #     'posts': Post.objects.all()
#     # }
    # name = request.GET.get('name')

    # new_entry = {
    #     'name': name,

    # }
    # ApiCall.objects.create(**new_entry)
    # return render(request, 'blog/create.html')
 
 
 
 
 
 
 
    # form = ApiCallForm(request.POST or None)
    # if form.is_valid():
    #     form.save()

    # context = {
    #     'form': form
    # })