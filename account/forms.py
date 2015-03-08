from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField

from account.models import Account


__author__ = 'k1'


# This forms used in AccountAdmin
class AccountCreationForm(UserCreationForm):
    """
    A Form for Creating new users. Includes all the required fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'photo')
        # fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            Account._default_manager.get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match !')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
        return user


class AccountChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label="Password",
        required=True,
        help_text="Raw passwords are not stored, so there is no way to see this user's"
                  "password,but you can change the password using "
                  "<a href=\"password/\"\>This Form </a> :D")

    class Meta(UserChangeForm.Meta):
        model = Account
        fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # this is done here, rather than on the field, because the field does not have access to the initial value
        return self.initial["password"]
