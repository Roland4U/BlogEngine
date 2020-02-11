from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .utils import *
from .models import *
from .forms import *

def main(srequest):
    return HttpResponse('Main page')

class PostList(ObjListMix, View):
    model = Post
    template = 'blog/post_list.html'

class PostDet(ObjDetMix, View):
    model = Post
    template = 'blog/post_det.html'

class PostCreate(ObjCreateMix, View):
    form = PostForm
    template = 'blog/new_post_form.html'

class PostEdit(ObjEditMix, View):
    model = Post
    form = PostForm
    template = 'blog/edit_post_form.html'

class PostDel(ObjDeleteMix, View):
    model = Post
    template = 'blog/post_del.html'

class TagList(ObjListMix, View):
    model = Tag
    template = 'blog/tag_list.html'

class TagDet(ObjDetMix, View):
    model = Tag
    template = 'blog/tag_det.html'

class TagCreate(ObjCreateMix, View):
    form = TagForm
    template = 'blog/new_tag_form.html'

class TagEdit(ObjEditMix, View):
    model = Tag
    form = TagForm
    template = 'blog/edit_tag_form.html'