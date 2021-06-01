from django.contrib import admin
from .models import Negociator, Map, Route
# Register your models here.

admin.site.register(Negociator, Map, Route)

