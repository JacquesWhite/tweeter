from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tweet(models.Model):
    content = models.TextField(verbose_name="Tweet")
    add_date = models.DateTimeField(verbose_name="add date", blank=True, default=timezone.now)
    author = models.ForeignKey(User, verbose_name="author", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-add_date',)

    def __str__(self):
        return u'%(content)s' % {
            u'content': self.content
        }

    @staticmethod
    def get_absolute_url():
        return '/feed'
