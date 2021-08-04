from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostDeleteView,
    AjaxHandlerView,
    PostUpdateView,
    ActView
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
    path('picture/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('picture/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('picture/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('about/', views.about, name='blog-about'),
    path('create/', ActView.as_view(), name='blog-create'),
    path('favorite/', views.link_view, name='blog-favorite'),
    path('select/', AjaxHandlerView.as_view(), name='blog-ajax'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
