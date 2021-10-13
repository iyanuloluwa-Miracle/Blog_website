#from django import template
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Post
# Create your views here.

def homeView(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    #template = loader.get_template('index.html')
    return render(request,'blog/index.html',context)

def detailView(request,post_id):
    post = get_object_or_404(Post,id= post_id)
    context = {
        'post':post
    }
    return render(request,'blog/detail.html',context)   