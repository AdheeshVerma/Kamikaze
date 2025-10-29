from django.urls import path
from typing import Any, cast
from . import views
urlpatterns = [
    path('', views.welcomeMsg),
    path('register/', cast(Any, views.register_user)),
    path('login/',cast(Any,views.login_user)),
]