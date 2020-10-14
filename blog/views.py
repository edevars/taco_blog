from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


class PostList(ListView):
    # Only shows the published posts, in status 1
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
