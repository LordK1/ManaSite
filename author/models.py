from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from sorl.thumbnail import ImageField


class Author(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    photo = ImageField(upload_to='users')

    def __str__(self):
        return "%s - %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.__str__()


# create our user object to attach our Author object
def create_author_user_callback(sender, instance, **kwargs):
    author, new = Author.objects.get_or_create(user=instance)

post_save.connect(create_author_user_callback, User)