from django.contrib import admin
from .models import Property, Comment
# Register your models here.

admin.site.register(Property, Comment)
