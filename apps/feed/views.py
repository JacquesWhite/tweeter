from django.views.generic import CreateView, ListView

from .models import Tweet
from ..tweeterprofile.models import User


class TweetCreateView(CreateView):
    model = Tweet
    fields = ['content']
    template_name = 'search/feed-with-search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.all()[:10]
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserTweetListView(ListView):
    model = Tweet
    fields = ['content']
    template_name = 'feed.html'

    def get_context_data(self, **kwargs):
        print(User.objects.last().id)
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.filter(author=self.kwargs['user'])
        return context
