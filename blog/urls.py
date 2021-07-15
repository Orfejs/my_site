from django.urls import path
from .views import (
    PostListView,
    PostDetailView
)
from . import views

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('create/', views.create, name='blog-create'),
    path('activity/', views.activity, name='blog-activity'),
    path('favorite/', views.favorite, name='blog-favorite')
   ]