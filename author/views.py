from django.views.generic import FormView, DetailView

from django.views.generic.list import ListView

from author.forms import ContactForm

from author.models import Author


class AuthorListView(ListView):
    template_name = 'author/author_list.html'
    model = Author
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all().order_by('get_posts')


class AuthorDetailView(DetailView):
    template_name = 'author/author_detail.html'
    model = Author
    context_object_name = 'author'