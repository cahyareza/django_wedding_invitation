from django.urls import path
from . import views

urlpatterns = [
    path("password_change", views.password_change, name="password_change"),
]