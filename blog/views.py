from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView
# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['without_category'] = Post.objects.filter(category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['without_category'] = Post.objects.filter(category=None).count()

        return context


class PostListByCategory(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(PostListByCategory, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)
            context['title'] = 'Blog - {}'.format(category.name)

        context['category'] = category

        return context


# def post_detail(request, pk) :
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/blog_post.html', {'post' : post})


# def index(request) :
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', { 'posts' : posts})

