from django.urls import path
from .views import (
    register, update, myportofolio
)

urlpatterns = [
    path("register/", register, name="register"),
    path('update/<slug:slug>/', update, name='update'),
    path('myportofolio/', myportofolio, name='myportofolio'),
]
