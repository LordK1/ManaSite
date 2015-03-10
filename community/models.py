from django.db import models

# Create your models here.
from author.models import Author
from post.models import Post


class Follow(models.Model):
    follower = models.ForeignKey(Author, related_name='follower')
    followed = models.ForeignKey(Author, related_name='followed')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s followed %s" % (self.followed, self.follower)


class LikeManager(models.Manager):
    def create_for_post(self, post, author):
        like_set = self.filter(post=post, author=author)
        # print('like_set', like_set)
        if not like_set:
            like = Like(post=post, author=author)
            like.numerator += 1
            like.save()
        else:
            like = like_set[0]
            like.numerator += 1
            like.save()
        return like

    def likes_by_post(self, post):
        """
        Count Likes for specified Post instance
        :param post:
        :return:
        """
        like = self.get(post=post)

        return like.numerator

    def get_queryset(self, post):
        return super(LikeManager, self).get_queryset().filter(post=post)


class Like(models.Model):
    author = models.ForeignKey(Author, related_name='likes')
    post = models.ForeignKey(Post, related_name='likes')
    numerator = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = LikeManager()

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ('author', 'post')

    def __str__(self):
        return "%s Liked Post.pk %d " % (self.author.get_full_name(), self.post.pk)

