from django.contrib import admin
from .models import CustomUser, Anime, AnimeList, AnimeListEntry, Discussion, DiscussionReplies

admin.site.register(CustomUser)
admin.site.register(Anime)
admin.site.register(AnimeList)
admin.site.register(AnimeListEntry)
admin.site.register(Discussion)
admin.site.register(DiscussionReplies)