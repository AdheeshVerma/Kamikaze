from django.db import models
from django.core.validators import RegexValidator

email_regex = RegexValidator(
        regex=r'/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/',
        message="email must be in the format example@gmail.com"
    )

class Personas(models.TextChoices):
    NOVICE = "n", "Novice"
    OTAKU = "o", "Otaku"
    WEABOO = "w", "Weeb"

class User(models.Model):
    username= models.CharField(max_length=15,name="username",unique=True,db_index=True,editable=False)
    tagline= models.CharField(max_length=200,name="tagline")
    password=models.CharField(name="password",null=False)
    email= models.CharField(name="email",unique=True,null=False,db_index=True)
    persona_name= models.CharField(name="persona_name",choices=Personas.choices, default=Personas.NOVICE)
    last_online=models.DateTimeField(name="last_online",auto_now=True)
    pfp= models.CharField(name="pfp")
    banner=models.CharField(name="banner")
    created_at = models.DateTimeField(name="created_at",editable=False,auto_now_add=True)
    updated_at =  models.DateTimeField(name="updated_at",editable=False,auto_now=True)