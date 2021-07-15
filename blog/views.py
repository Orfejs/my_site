import json
import os.path
from django.shortcuts import render
import requests
from django.views.generic import ListView, DetailView
from .models import Post
from .models import ApiCall
from .forms import ApiCallForm
from .models import Activity


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class ApiCallView(DetailView):
    model = ApiCall
    template_name = 'blog/create_api.html'
    context_object_name = 'apicalls'
    ordering = ['like = True']


def about(request):
    response = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
    picture = response.json()
    my_picture = picture[0]
    random_pic = my_picture['urls']
    return render(request, 'blog/about.html', {
        'img': random_pic['regular']

    }
                  )

def create(request):
    response = requests.get(
        'https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
    picture = response.json()
    my_picture = picture[0]
    random_pic = my_picture['urls']
    reg_pic = random_pic['regular']
    b = ApiCall(name = reg_pic)
    b.save()
    return render(request, 'blog/create_api.html')

def activity(request):
    response1 = requests.get('https://www.boredapi.com/api/activity')
    task = response1.json()
    random_task = task['activity']
    c = Activity(name = random_task)
    c.save()
    return render(request, 'blog/activity.html', {
        'todo': random_task

    })

def favorite(request):
    context = {
    'apicalls': ApiCall.objects.filter(likes=True)
    }
    return render(request, 'blog/favorite.html', context)


    # form = ApiCallForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #
    # context = {
    #     "form": form
    # }
    # return render(request, 'blog/create_api.html', context)
