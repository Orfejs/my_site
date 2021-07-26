from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    ListView,
    DetailView
    )
import requests
from .models import Post
from .models import ApiCall
from .models import Activity



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


class AjaxHandlerView(View):
    template_name = 'blog/ajax.html'

    def get(self, request):
        answer = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
        reg_img = answer.json()
        my_pic = reg_img[0]['urls']['regular']

            # text = request.GET.get('test')
        if request.is_ajax():
            return JsonResponse({'question': my_pic}, status=200)
        return render(request, 'blog/home.html')

    def post(self, request):
        card = request.POST.get('test2')
        b = ApiCall(name=card, favorite=True)
        b.save()
        return JsonResponse({'good': card}, status=200)


def act1(request):
    # car = request.POST.get('test3')
    response1 = requests.get('https://www.boredapi.com/api/activity')
    task = response1.json()
    random_task = task['activity']
    c = Activity(name=random_task)
    c.save()

    return render(request, 'blog/create.html', {
            'todo': random_task
            })


def about(request):
    response = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
    picture = response.json()
    my_picture = picture[0]
    random_pic = my_picture['urls']
    return render(request, 'blog/about.html', {
        'img': random_pic['regular']

        
    })


# def activity(request):
#




def link_view(request):
    context = {
        'apicalls': ApiCall.objects.filter(favorite=True)
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