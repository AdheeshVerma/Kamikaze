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
    username= models.CharField(max_length=15,db_column="username",unique=True,db_index=True,editable=False)
    tagline= models.CharField(max_length=200,db_column="tagline")
    password=models.CharField(db_column="password",null=False,)
    email= models.CharField(db_column="email",unique=True,null=False,db_index=True)
    persona_name= models.CharField(db_column="persona_name",choices=Personas.choices, default=Personas.NOVICE)
    last_online=models.DateTimeField(db_column="last_online",auto_now=True)
    pfp= models.CharField(db_column="pfp")
    banner=models.CharField(db_column="banner")
    created_at = models.DateTimeField(db_column="created_at",editable=False,auto_now_add=True)
    updated_at =  models.DateTimeField(db_column="updated_at",editable=False,auto_now=True)