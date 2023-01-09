from django.urls import path

from .views import photo_list

urlpatterns = [
    path('', photo_list, name='photo_list'),
]