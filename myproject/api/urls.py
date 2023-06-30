from django.urls import path, include

app_name = "api"
urlpatterns = [
    path('portofolio/', include('myproject.api.portofolio.urls')),
]