from django.urls import path
from . import views
from .genre_seed import populate_genres
from typing import Any, cast
urlpatterns = [
    path('',views.welcomeMsg),
    path('create-user/',cast(Any,views.add_new_user)),
    path('get-all-users/',cast(Any,views.get_all_user)),
    path('get-user-by-id/',cast(Any,views.get_user_by_id)),
    path('populate-db/',cast(Any,populate_genres))
]   