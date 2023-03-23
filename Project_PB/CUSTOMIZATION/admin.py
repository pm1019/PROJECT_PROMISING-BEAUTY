from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Dress


admin.site.register(Dress)