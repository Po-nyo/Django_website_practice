from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class PostList(ListView) :
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-date')


class PostDetail(DetailView) :
    model = Post


# def post_detail(request, pk) :
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/blog_post.html', {'post' : post})


# def index(request) :
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', { 'posts' : posts})

