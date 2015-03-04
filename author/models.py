from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from sorl.thumbnail import ImageField


class Author(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
    photo = ImageField(upload_to='users')

    def __str__(self):
        return "%s - %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('author-profile', kwargs={'pk': self.pk})