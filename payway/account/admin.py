from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "account_number",
        "currency",
        "balance",
        "is_approved",
    ]
    list_display_links = list_display[:-1]

    search_fields = ["user", "account_number"]
    list_filter = ["currency"]
