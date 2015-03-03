from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from author.forms import RegistrationForm, ContactForm


class RegistrationFormView(FormView):
    template_name = 'author/registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed
        # It should return an HttpResponse
        print('<><<><><<><><><><><> form is valid  !')

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'])

        user.save()
        author = form.save(commit=False)
        # commit=False tells Django that "Don't send this to database yet.
        # I have more things I want to do with it."
        author.user = self.request.user
        author.save()

        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        print('=)=)=)=)=)=)=)=)=)=)=)=)=)=)=)  form invalid called !!!')
        return super(RegistrationFormView, self).form_invalid(form)

        # def post(self, request, *args, **kwargs):
        # print('>>>>>>>>>>>>>>>>>>>>>>>>> form post method called !!!', request.user.is_authenticated())
        #
        #     if request.user.is_authenticated():
        #         return HttpResponseRedirect(self.success_url)
        #     form = RegistrationForm(self.request.POST)
        #     if form.is_valid():
        #         user = User.objects.create_user(username=form.cleaned_data['username'],
        #                                         password=form.cleaned_data['password'],
        #                                         email=form.cleaned_data['email'])
        #         user.save
        #
        #     return super(RegistrationFormView, self).post(request, *args, **kwargs)


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