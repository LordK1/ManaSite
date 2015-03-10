from braces.views import JSONResponseMixin, AjaxResponseMixin, LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView

from author.models import Author
from community.models import Like
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
        # print('get_ajax', post, ' USer : ', request.user)
        author = Author.objects.get(account=request.user)
        # print('Author', author)

        like = Like.objects.create_for_post(post, author)
        print('like', like.numerator, 'likes : ', Like.objects.get(post=post).numerator)

        data = {
            'title': post.title,
            'slug': post.slug,
            'id': post.id,
        }

        return self.render_json_response(data)


class DisLikePostView(JSONResponseMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        print('DisLikePostView', kwargs.get('pk'))
