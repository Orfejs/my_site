from django.http import JsonResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              redirect,
                                HttpResponseRedirect)
from django.views.generic import (
    View,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
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
    List all apicalls, or create a new apicall.
    """
    def get(self, request, format=None):
        apicalls = ApiCall.objects.all()
        serializer = ApiCallSerializer(apicalls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApiCallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, ):
    #     apicall_data = request.data
    #     print(apicall_data)
    #
    #     new_apicall = ApiCall.objects.create(apicallid=apicall_data["20"], apicall_name=apicall_data[
    #         "somevalue"], favorite=apicall_data["True"])
    #
    #     print(new_apicall)
    #
    #     new_apicall.save()
    #
    #     serializer = ApiCallSerializer(new_apicall)
    #
    #     return Response(serializer.data)
    #


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
    model = ApiCall


class PostUpdateView(UpdateView):
    model = ApiCall
    fields = ['favorite']
    success_url = '/'


class PostDeleteView(DeleteView):
    model = ApiCall
    success_url = '/'

    def test_func(self):
        apicall = self.get_object()
        print(apicall)
        if self.request.user == apicall.id:
            return True
        return False


class ApiCallView(DetailView):
    model = ApiCall
    template_name = 'blog/link.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'apicalls'
    ordering = 'date_posted'


class AjaxHandlerView(View):
    template_name = 'blog/ajax.html'

    def get(self, request):
        answer = requests.get('https://api.unsplash.com/photos/random/?client_id=GvDLAzZDt1_Ba2E8l_DDiPNxlmJwKOTJbd5w5kZ-YH8&count=1')
        reg_img = answer.json()
        my_pic = reg_img[0]['urls']['regular']

            # text = request.GET.get('test')
        if request.is_ajax():
            return JsonResponse({'question': my_pic}, status=200)
        return render(request, 'blog/ajax.html')

    def post(self, request):
        card = request.POST.get('test2')
        b = ApiCall(name=card, favorite=True)
        b.save()
        return JsonResponse({'good': card}, status=200)


class ActView(View):
    def get(self, request):
        response1 = requests.get('https://www.boredapi.com/api/activity')
        task = response1.json()
        random_task = task['activity']
        return render(request, 'blog/create.html', {
               'todo': random_task
                })

    def post(self, request):
        front = request.POST.get('test3')
        print(front)
        c = Activity(name=front)
        c.save()
        return JsonResponse({'well': front}, status=200)


def link_view(request):
    context = {
        'apicalls': ApiCall.objects.filter(favorite=True).order_by('-date_posted')
    }
    return render(request, 'blog/link.html', context)


def apicall_delete(request):
    cat = request.POST.get('test4')  # Get your current cat
    print(cat)
    if request.method == 'POST':         # If method is POST,
        cat.delete()                     # delete the cat.
        return redirect('/')             # Finally, redirect to the homepage.

    return render(request, 'blog/link.html', {'cat': cat})
