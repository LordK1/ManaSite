from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from post.models import Post, Category


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = kwargs
        context['posts'] = Post.objects.all().order_by('-created_date')[:5]
        return context


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = '5'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'


class CategoryListView(ListView):
    model = Category
    template_name = 'post/category_list.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'
    paginate_by = '5'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'post/category_detail.html'
    context_object_name = 'category'