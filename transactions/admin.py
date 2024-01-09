from django.contrib import admin

from .models import Transactions, Deposit


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "account_number",
        "transaction_type",
        "amount",
        "status",
    ]
    list_display_links = list_display[:2]
    search_fields = ["user", "account_number"]
    list_filter = ["status"]
