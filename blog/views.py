from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'contents', 'head_image', 'category', 'tags']


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'contents', 'head_image', 'category', 'tags']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self), self).form_valid(form=form)
        else:
            return redirect('/blog/')


class PostListByTag(ListView):
    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=tag_slug)

        return tag.post_set.order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListByTag, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['without_category'] = Post.objects.filter(category=None).count()
        tag_slug = self.kwargs['slug']
        context['tag'] = Tag.objects.get(slug=tag_slug)

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

