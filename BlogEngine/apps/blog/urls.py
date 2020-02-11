from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name="index"),
    path('post/new', PostCreate.as_view(), name="post_new"),
    path('post/<str:slug>', PostDet.as_view(), name="post_det"),
    path('post/<str:slug>/edit', PostEdit.as_view(), name="post_edit"),
    path('post/<str:slug>/del', PostDel.as_view(), name="post_del"),
    path('tag/new', TagCreate.as_view(), name="tag_new"),
    path('tag/<str:slug>', TagDet.as_view(), name="tag_det"),
    path('tag/<str:slug>/edit', TagEdit.as_view(), name="tag_edit"),
    path('tags', TagList.as_view(), name="tag_list"),
]
