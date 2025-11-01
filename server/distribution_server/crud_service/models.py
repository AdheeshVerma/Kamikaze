from operator import length_hint

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

email_regex = RegexValidator(
    regex=r'/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/',
    message="email must be in the format example@gmail.com"
)


class Personas(models.TextChoices):
    NOVICE = "n", "Novice"
    OTAKU = "o", "Otaku"
    WEABOO = "w", "Weeb"


class Genres(models.TextChoices):
    ACTION = "AC", "Action"
    HORROR = "HO", "Horror"
    ROMANCE = "RO", "Romance"
    SHONEN = "SH", "Shonen"


class ListType(models.TextChoices):
    COMPLETED = "C", "Completed"
    ONGOING = "O", "Ongoing"


# Will be changed im not sure about the types yet
class ListEntryType(models.TextChoices):
    COMPLETED = "C", "Completed"
    ONGOING = "O", "Ongoing"


class Anime(models.Model):
    name = models.TextField(verbose_name=("anime_name"), max_length=50)
    jikan_id = models.CharField(verbose_name="jikan_id", max_length=255)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, name="username", unique=True, editable=False)
    tagline = models.CharField(max_length=200, name="tagline")
    password = models.CharField(max_length=50, name="password", null=False)
    email = models.CharField(max_length=100, name="email", unique=True, null=False, db_index=True)
    persona_name = models.CharField(max_length=25, name="persona_name", choices=Personas.choices, default=Personas.NOVICE)
    last_online = models.DateTimeField(name="last_online", auto_now=True)
    pfp = models.CharField(max_length=255, name="pfp")
    banner = models.CharField(max_length=255, name="banner")
    created_at = models.DateTimeField(name="created_at", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(name="updated_at", editable=False, auto_now=True)

    def _str_(self):
        return f"{self.username}"

class AnimeList(models.Model):
    name = models.TextField(verbose_name="ListName", max_length=25, null=False)
    description = models.TextField(verbose_name="description")
    types = models.TextField(verbose_name="types", choices=ListType.choices, default=ListType.ONGOING)
    createdBy = models.ForeignKey(CustomUser, verbose_name="created_by", null=False ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="created_at", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", editable=False, auto_now=True)

    def _str_(self):
        return f"{self.name}"


class AnimeListEntry(models.Model):
    list_id = models.ForeignKey("AnimeList", verbose_name="list_id", on_delete=models.CASCADE)
    anime_id = models.ForeignKey("Anime", verbose_name="anime_id", on_delete=models.CASCADE)
    status = models.TextField(verbose_name=("status"), choices=ListEntryType.choices, max_length=50)
    review = models.TextField(verbose_name=("review"), null=True)
    rating = models.IntegerField(verbose_name=("rating"), choices=[(i, str(i)) for i in range(1, 6)])

    # def _str_(self):
    #     return f"{self.name}"


class Discussion(models.Model):
    title = models.TextField(verbose_name=("title"), max_length=50)
    description = models.TextField(verbose_name=("description"))
    created_by = models.ForeignKey("CustomUser", verbose_name=("created_by"), null=False, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.title}"


class DiscussionReplies(models.Model):
    reply = models.TextField(verbose_name=("reply"), max_length=500)
    discussion_id = models.ForeignKey("Discussion", verbose_name="discussion_id", on_delete=models.CASCADE)
    created_by = models.ForeignKey("CustomUser", verbose_name="created_by", null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="created_at", editable=False, auto_now_add=True)