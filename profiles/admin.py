from django.contrib import admin
from .models import Profiles


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "account_number", "country", "currency"]
    list_display_links = list_display[:2]
    search_fields = ["account_number"]
    list_filter = ["currency", "country"]
