from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.views.generic import FormView, TemplateView, DetailView
from django.views.generic.list import ListView

from author.forms import RegistrationForm, ContactForm
from author.models import Author


class RegistrationFormView(FormView):
    template_name = 'author/registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def __init__(self, **kwargs):
        super(RegistrationFormView, self).__init__(**kwargs)

    def form_valid(self, form):
        print(' form is valid  !')
        form.send_email()

        if self.request.user.is_authenticated():
            return HttpResponseRedirect('/')

        user = User.objects.create_user(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'),
            email=form.cleaned_data.get('email'))

        user.save()
        author = form.save(commit=False)
        author.user = user
        author.photo = self.get_form_kwargs().get('files').get('photo')
        # self.id = author.pk
        author.save()
        if user is not None:
            if user.is_active():
                login(self.request, user)
                return HttpResponseRedirect(author.get_absolute_url())
            else:
                # Return a 'disabled account' error message
                return HttpResponseRedirect("Return a 'disabled account' error message")
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect("Return an 'invalid login' error message.")

    def form_invalid(self, form):
        print(' form invalid called !!!')
        return super(RegistrationFormView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('author-profile', kwargs={'pk': self.id})


class ContactFormView(FormView):
    template_name = 'author/contact_form.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print('subject', self.request.POST['subject'])
        print('message', self.request.POST['message'])
        print('sender', self.request.POST['sender'])
        print('cc_myself', self.request.POST['cc_myself'])
        form.send_email()
        return super(ContactFormView, self).form_valid()


class AuthorListView(ListView):
    template_name = 'author/list.html'
    model = Author
    context_object_name = 'authors'


class AuthorProfile(DetailView):
    template_name = 'author/profile.html'
    model = Author
    context_object_name = 'author'


def login(request):
    if request.method != 'POST':
        raise Http404('Only POST are allowed !!!')
    try:
        author = Author.objects.get(username=request.POST.get('username'))
        if author.user.password == request.POST.get('password'):
            request.session['author_id'] = author.id
            return HttpResponseRedirect(author.get_absolute_url())
    except Author.DoesNotExist:
        return HttpResponseRedirect("Your username and password didn't match.")


def logout(request):
    try:
        del request.session['author_id']
    except KeyError:
        pass
    return HttpResponseRedirect("/")





