from django.urls import path
from typing import Any, cast
from . import views
from crud_service.seed_data import populate_api_data

urlpatterns = [
    path('', views.welcomeMsg),
    path('register/', cast(Any, views.register_user)),
    path('login/',cast(Any,views.login_user)),
    path('populate-db/',cast(Any,populate_api_data))
]