from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from author.models import Author

__author__ = 'k1'


class RegistrationForm(ModelForm):
    username = forms.CharField(label=u'User Name',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'usernameInput',
                                                             'placeholder': 'Enter your new UserName'}))

    email = forms.EmailField(label=u'Email Address',
                             widget=forms.TextInput(
                                 attrs={'type': 'email',
                                        'class': 'form-control',
                                        'id': 'emailInput',
                                        'placeholder': 'Enter your Email Adderss !'}))

    password = forms.CharField(label=u'Password',
                               widget=forms.PasswordInput(render_value=False,
                                                          attrs={'class': 'form-control',
                                                                 'id': 'passwordInput',
                                                                 'placeholder': 'enter your passowrd'}),
                               help_text='please enter your password')

    verify_password = forms.CharField(label=u'Verify Password',
                                      widget=forms.PasswordInput(render_value=False,
                                                                 attrs={'class': 'form-control',
                                                                        'id': 'verifyPasswordInput',
                                                                        'placeholder': 'enter again password !'}),
                                      help_text='re enter above password')

    class Meta:
        model = Author
        fields = ['username', 'email', 'password', 'verify_password', 'first_name', 'last_name', ]

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, Please use another username :'P ")

    def clean_password(self):
        password = self.cleaned_data['password']
        # verify_password = self.cleaned_data['verify_password']

        # if password != verify_password:
        #     raise forms.ValidationError('Password and Verify Password fields did not match , please try again !')
        return password

    # def send_email(self):
    #     print('send_email called username : ', self.username, ' email : ', self.email, ' password : ', self.password,
    #           ' verify_password : ', self.verify_password)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['email', 'first_name', 'last_name']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        print('send_email called subject : ', self.subject, ' message : ', self.message, ' sender : ', self.sender,
              ' cc_myself : ', self.cc_myself)