from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    AjaxHandlerView,
   )
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('call', views.CallView, basename='calls')


urlpatterns = [
    path('apicalls/', views.ApiCallList.as_view()),
    path('apicalls/<int:pk>/', views.CallView.as_view(), name='api-home'),
    # path('', include(router.urls)),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
    path('create/', views.act1, name='blog-create'),
    path('favorite/', views.link_view, name='blog-favorite'),
    path('ajax/', AjaxHandlerView.as_view(), name='blog-ajax'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
