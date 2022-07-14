import django.utils.functional
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import RegisteredUser, FeedItem


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request, filter_by='all_posts') -> django.shortcuts.render:
    template_name = "users/index.html"
    user = request.user
    match filter_by:
        case 'my_posts':
            feed_items = FeedItem.objects.filter(user=user)
        case 'peoples_posts':
            feed_items = get_peoples_posts(user)
        case _:
            feed_items = FeedItem.objects.all()
    context = {
        'feed_items': feed_items,
    }
    if user.is_authenticated and not RegisteredUser.objects.filter(user=user):
        RegisteredUser(user=user).save()
    return render(request, template_name, context)


def get_peoples_posts(user: django.utils.functional.SimpleLazyObject) -> list:
    users_followed = RegisteredUser.objects.get(user=user).tracking.all()
    feed_items = []
    for user_followed in users_followed:
        feed_items.extend(FeedItem.objects.filter(user=user_followed.user))
    return feed_items
