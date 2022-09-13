from django.urls import path
from .views import (
    register, update
)

urlpatterns = [
    path("register/", register, name="register"),
    path('<int:id>/', update, name='update'),
]
