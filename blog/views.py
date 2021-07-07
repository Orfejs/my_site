from django.shortcuts import render
import requests
from .models import Post




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    response = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
    picture = response.json()
    my_picture = picture[0]
    random_pic = my_picture['urls']
    return render(request, 'blog/about.html', {
        'img': random_pic['regular']
    })