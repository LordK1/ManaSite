import os
from django.core.urlresolvers import reverse
from django.db import models
from sorl.thumbnail import ImageField
from ManaSite.settings import MEDIA_ROOT
from author.models import Author

STATUS_CHOICES = (('A', 'Active'), ('P', 'Pending'), ('D', 'De Active'))

UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'photos')


class CategoryManager(models.Manager):
    pass


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    objects = CategoryManager()

    class Meta:
        app_label = 'post'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def get_post_count(self):
        return self.posts.all().count()


class PostManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()
        

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    lead = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(unique=True, blank=False)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='posts')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    photo = ImageField(upload_to='photos')
    authors = models.ManyToManyField(Author, related_name='posts', verbose_name='List of Authors')
    objects = PostManager()

    class Meta:
        app_label = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_authors(self):
        return self.authors.all()
