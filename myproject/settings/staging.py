from ._base import *

DEBUG = False
WEBSITE_URL = "https://www.myproject.192.168.56.6.nip.io/home"  # without trailing slash
WEBSITE_URL_FRONTEND = "https://www.myproject.192.168.56.6.nip.io/"
NAMA_DOMAIN = "www.myproject.192.168.56.6.nip.io"
CORS_ALLOWED_ORIGINS = [
    "https://www.myproject.192.168.56.6.nip.io", "http://192.168.56.20"
]
ALLOWED_HOSTS = [
    "*",
]
