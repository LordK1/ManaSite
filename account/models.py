from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from sorl.thumbnail import ImageField


class AccountManager(BaseUserManager):
    def get_queryset(self):
        return super(AccountManager, self).get_queryset()

    def get_author_by_natural_key(self, username):
        return super(AccountManager, self).get_by_natural_key(username).author

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address !')
        if not username:
            raise ValueError('Users must have an username !')
        user = self.model(username=username, email=self.normalize_email(email), )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


GENDER_CHOICES = (('male', 'Male'),
                  ('female', 'Female'))


# Customized User class
class Account(AbstractBaseUser, PermissionsMixin):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]', message='Only numeric characters are allowed !!!')

    # Redefine the basic fields that would normally be defined in User ###
    username = models.CharField(unique=True, max_length=20, validators=[alphanumeric])
    email = models.EmailField('email address', unique=True, max_length=255)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    # Our own fields
    birthday = models.DateTimeField(auto_now_add=True)
    biography = models.CharField(max_length=600, blank=True)
    photo = ImageField(upload_to='accounts', blank=False, null=False, default="/static/images/13.jpg")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.email



