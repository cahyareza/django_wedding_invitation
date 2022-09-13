from django.urls import path
from .views import (
    register, update
)

urlpatterns = [
    path("register/", register, name="register"),
    path('update/<int:id>/', update, name='update'),
]
