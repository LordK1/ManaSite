from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, DetailView

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

        # if self.request.user.is_authenticated():
        # return HttpResponseRedirect('/')

        user = User.objects.create_user(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'),
            email=form.cleaned_data.get('email'))

        user.save()
        author = form.save(commit=False)
        author.user = user
        author.photo = self.get_form_kwargs().get('files').get('photo')
        self.id = author.pk
        author.save()

        return HttpResponseRedirect(author.get_absolute_url())

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


class AuthorProfile(DetailView):
    template_name = 'author/profile.html'
    model = Author
    context_object_name = 'author'

