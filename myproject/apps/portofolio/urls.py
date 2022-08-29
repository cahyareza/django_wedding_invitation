# myproject/apps/ideas/urls.py
from django.urls import path
from .views import (
    register_couple
)

urlpatterns = [
    path("register/", register_couple, name="register"),
]
