from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class AuthorManager(models.Manager):
    def create_from_account(self, account):
        author = self.create(account=account)
        # do something with the author
        author.save()
        return author


class Author(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL)
    post_count = models.PositiveIntegerField(default=0)
    last_post_publish_date = models.DateTimeField(auto_now_add=True)

    objects = AuthorManager()

    def __str__(self):
        return self.account.email

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def get_categories(self):
        result_list = []
        for post in self.posts.all():
            result_list.append(post.category)
        return result_list

    def get_post_count(self):
        return self.posts.all().count()

    def get_full_name(self):
        return self.account.get_full_name()

