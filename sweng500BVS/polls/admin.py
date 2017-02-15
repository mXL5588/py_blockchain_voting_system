from django.contrib import admin

# Register your models here.

from .models import Ballot

admin.site.register(Ballot)