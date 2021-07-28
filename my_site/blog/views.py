from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    ListView,
    DetailView
    )
import requests
from django.http import Http404
from .models import Post
from .models import ApiCall
from .models import Activity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApiCallSerializer


class ApiCallList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        apicalls = ApiCall.objects.all()
        serializer = ApiCallSerializer(apicalls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.GET)

        serializer = ApiCallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallView(APIView):

    def get_object(self, pk):
        try:
            return ApiCall.objects.get(pk=pk)
        except ApiCall.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        apicall = self.get_object(pk)
        serializer = ApiCallSerializer(apicall)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):

        try:
            id = request.query_params["id"]
            if id != None:
                apicall = ApiCall.objects.get(id=id)
                serializer = ApiCallSerializer(apicall)
        except:
            apicalls = self.get_queryset()
            serializer = ApiCallSerializer(apicalls, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        apicall_data = request.data

        new_apicall = ApiCall.objects.create(apicallid=apicall_data["20"], apicall_name=apicall_data[
            "somevalue"], favorite=apicall_data["True"])

        print(new_apicall)


        new_apicall.save()

        serializer = ApiCallSerializer(new_apicall)

        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return ApiCall.objects.get(pk=pk)
        except ApiCall.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        apicall = self.get_object(pk)
        serializer = ApiCallSerializer(apicall)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        apicall = self.get_object(pk)
        apicall.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get(self, request, format=None):
    #     apicalls = ApiCall.objects.all()
    #     serializer = ApiCallSerializer(apicalls, many=True)
    #     return Response(serializer.data)



# class ApiCallView(viewsets.ViewSet):
#     def list(self, request):
#         """Return a hello message."""
#
#         a_viewset = [
#             'Uses actions (list, create, retrieve, update, partial_update)',
#             'Automatically maps to URLS using Routers',
#             'Provides more functionality with less code',
#         ]
#
#         return Response({'message': 'Hello!', 'a_viewset': a_viewset})


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