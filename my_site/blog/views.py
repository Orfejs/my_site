from django.shortcuts import render
import requests

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
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