from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, EmailField, TextInput, PasswordInput, FileField, FileInput, \
    ClearableFileInput
from author.models import Author

__author__ = 'k1'


class RegistrationForm(ModelForm):
    username = CharField(label=u'User Name',
                         widget=TextInput(attrs={'class': 'form-control',
                                                 'id': 'usernameInput',
                                                 'placeholder': 'Enter your new UserName'}))

    email = EmailField(label=u'Email Address',
                       widget=TextInput(
                           attrs={'type': 'email',
                                  'class': 'form-control',
                                  'id': 'emailInput',
                                  'placeholder': 'Enter your Email Adderss !'}))

    password = CharField(label=u'Password',
                         widget=PasswordInput(render_value=False,
                                              attrs={'class': 'form-control',
                                                     'id': 'passwordInput',
                                                     'placeholder': 'enter your passowrd'}),
                         help_text='please enter your password')

    confirm_password = CharField(label=u'Confirm Password',
                                 widget=PasswordInput(render_value=False,
                                                      attrs={'class': 'form-control',
                                                             'id': 'confirmPasswordInput',
                                                             'placeholder': 'enter again password !'}),
                                 help_text='re enter above password')

    first_name = CharField(label=u'First Name', required=False,
                           widget=TextInput(attrs={'class': 'form-control', 'id': 'first_nameInput',
                                                   'placeholder': 'what is your First Name !?!?'}),
                           help_text='optional : enter your first name')

    last_name = CharField(label=u'Last Name', required=False,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'last_nameInput',
                                                        'placeholder': 'what is your Last Name !?!'}),
                          help_text='Optional enter your last Name !')

    photo = FileField(label=u'Photo', required=False,
                      widget=ClearableFileInput(attrs={'type': 'file',
                                                       'placeholder': 'change your profile photo'}),
                      help_text='Optional make photo as Avatar!')

    class Meta:
        model = Author
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'photo']

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
            raise ValidationError("Password and Confirm must match.")

        return self.cleaned_data

    def send_email(self):
        print(
            'send_email called username : ', self.cleaned_data.get('username'),
            ' email : ', self.cleaned_data.get('email'),
            ' password : ', self.cleaned_data.get('password'),
            ' confirm_password : ', self.cleaned_data.get('confirm_password'),
            ' photo : ', self.cleaned_data.get('photo')
        )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        print('send_email called subject : ', self.subject, ' message : ', self.message, ' sender : ', self.sender,
              ' cc_myself : ', self.cc_myself)