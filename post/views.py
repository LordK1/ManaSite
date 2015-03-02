from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from post.models import Post, Category


class HomePageView(TemplateView):
    template_name = 'home.html'


class PostListView(ListView):
    template_name = 'post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    context_object_name = 'post'


class CategoryListView(ListView):
    template_name = 'category_list.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    template_name = 'category_deatail.html'
    context_object_name = 'category'