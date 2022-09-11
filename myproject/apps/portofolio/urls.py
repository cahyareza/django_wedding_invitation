# myproject/apps/ideas/urls.py
from django.urls import path
from .views import (
    register, portofolio_detail
)

urlpatterns = [
    path("register/", register, name="register"),
    path('<int:id>/', portofolio_detail, name='portofolio_detail'),
]
