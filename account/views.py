from braces.views import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login as auth_login, logout as auth_logoout, authenticate
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import FormView, RedirectView, TemplateView
from account.forms import AccountCreationForm
from account.models import Account
from author.forms import AuthorForm
from author.models import Author


'''
------------------------------------------------------------
This Views added via watching GoDjango tutorials :
https://godjango.com/81-account-control-part-1/
thanks for watching :-P
'''


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'
    object = Account
    model = Account

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        account = self.object.objects.get_by_natural_key(self.request.user)
        context['user'] = account.get_full_name()
        context['account'] = account
        context['author'] = account.author
        context['posts'] = account.author.posts.all()
        context['likes'] = account.author.likes.all()
        return context

    def get_queryset(self):
        print('get_queryset', self.object.author_set.all())
        return self.object.objects.all()


# New LoginView with GoDjango tutorial helps
class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    permanent = False
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        auth_logoout(request)
        return super(LogoutView, self).get(request, args, kwargs)


class AccountRegistrationView(FormView):
    template_name = 'account/register.html'
    form_class = AccountCreationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        new_account = form.save()
        print(new_account)
        user = authenticate(
            username=new_account.email,
            password=form.cleaned_data.get('password1')
        )
        auth_login(self.request, user)
        # Create and Save an Instance of Author created new Account instance, maybe is wrong !!!
        author = Author.objects.create_from_account(new_account)
        print(author)
        return HttpResponseRedirect(self.get_success_url())


class PasswordRecoveryView(FormView):
    pass


class SettingsView(FormView):
    pass