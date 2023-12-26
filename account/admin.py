from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "account_number",
        "currency",
        "approved",
    ]
    list_display_links = list_display[:2]
    search_fields = ["user", "account_number"]
    list_filter = ["currency"]
