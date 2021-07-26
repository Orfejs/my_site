from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    AjaxHandlerView,
   )
from . import views





urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),
    path('create/', views.act1, name='blog-create'),
    path('favorite/', views.link_view, name='blog-favorite'),
    path('ajax/', AjaxHandlerView.as_view(), name='blog-ajax'),
]