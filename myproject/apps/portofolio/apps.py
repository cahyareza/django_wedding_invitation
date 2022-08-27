from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PortofolioConfig(AppConfig):
    name = "myproject.apps.portofolio"
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = _("Portofolio")