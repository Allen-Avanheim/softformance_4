from django.contrib import admin

from .models import RegisteredUser, FeedItem

admin.site.register(RegisteredUser)
admin.site.register(FeedItem)
