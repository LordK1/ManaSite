from braces.views import JSONResponseMixin, AjaxResponseMixin, LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView

from author.models import Author
from community.models import Like, Follow
from post.models import Post


def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    print(' like_post view ', pk, 'Post', post)
    data = {
        'pk': post.pk,
        'title': post.title,
        'slug': post.slug
    }
    return JsonResponse(data)


class LikePostView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, TemplateView):
    """
    When Like button clicked, one request sent and like counter should one pluse and then return total count of Likes,
    May be it's not true but i'll try it .
    """
    login_url = reverse_lazy('login')

    def get_ajax(self, request, *args, **kwargs):
        # print('get_ajax : ' + kwargs.get('pk'))
        post = Post.objects.get(pk=kwargs.get('pk'))
        print('get_ajax', post.id, ' USer : ', request.user)
        author = Author.objects.get(account=request.user)
        print('Author', author)

        like_set = Like.objects.filter(post=post, author=author)
        print('likes', like_set)
        if like_set.exists():
            print('liked before', like_set)
        else:
            Like(post=post, author=author).save()
            print("New Like saved : ", Like.objects.get(post=post, author=author))

        data = {
            'title': post.title,
            'slug': post.slug,
            'id': post.id,
            'likes': post.likes.count()
        }

        return self.render_json_response(data)


class DisLikePostView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, TemplateView):
    """
    When user Dislike specified post like should remove and count update.
    """
    login_url = reverse_lazy('login')

    def get_ajax(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs.get('pk'))
        author = Author.objects.get(account=request.user)
        like_set = list(Like.objects.filter(post=post, author=author))
        if like_set.exists():
            like = like_set[0]
            print('liked before ', like)
            like.delete()

        else:
            print('no Like find !!!')

        data = {
            'title': post.title,
            'slug': post.slug,
            'id': post.id,
            'likes': post.likes.count()
        }
        return self.render_json_response(data)


class FollowAuthorView(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, TemplateView):
    """
    When a user want to fallow a author must be logged in
    """
    login_url = reverse_lazy('login')

    def get_ajax(self, request, *args, **kwargs):
        followed = Author.objects.get(pk=kwargs.get('pk'))
        follower = Author.objects.get(account=request.user)

        if followed != follower:
            try:
                follow = Follow.objects.get(follower=follower, followed=followed)
                msg = 'follow found : ' + str(follow)

            except Follow.DoesNotExist:
                follow = Follow(follower=follower, followed=followed)
                follow.save()
                msg = 'New Follow saved !'

        else:
            msg = 'you cant follow yourself !!!'

        data = {
            'followed': followed.account.username,
            'follower': follower.account.email,
            'message': msg
        }

        return self.render_json_response(data)