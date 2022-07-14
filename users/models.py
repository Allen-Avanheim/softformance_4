from django.contrib.auth.models import User
from django.db import models


class Ownable(models.Model):
    user = models.ForeignKey('auth.User', verbose_name="Author",
                             related_name="%(class)ss",
                             on_delete=models.PROTECT)

    class Meta:
        abstract = True


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    tracking = models.ManyToManyField('self',
                                      related_name='tracked_by',
                                      blank=True, symmetrical=False)

    def __str__(self):
        return self.user.username


class FeedItem(Ownable):
    content = models.CharField("Content", max_length=1000,
                               blank=True, null=True)

    def __str__(self):
        return self.content[:50]
