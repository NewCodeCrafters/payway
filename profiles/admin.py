from django.contrib import admin
from .models import Profiles


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "country", "currency"]
    list_display_links = list_display[:2]
    list_filter = ["currency", "country"]
