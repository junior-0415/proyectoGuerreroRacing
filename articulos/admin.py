from atexit import register
from django.contrib import admin

from articulos.models import Articulos

# Register your models here.

admin.site.register(Articulos)