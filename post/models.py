from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    lead = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
