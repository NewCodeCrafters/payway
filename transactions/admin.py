from django.contrib import admin
from .models import Deposit, Transactions, InterwalletSwap, ExchangeRate, WalletTransfer


@admin.register(InterwalletSwap)
class InterWalletSwapAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "source_account",
        "target_account",
    ]
    list_display_links = list_display
    search_fields = list_display


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = [
        "source_currency",
        "target_currency",
        "rate",
    ]
    list_display_links = list_display
    search_fields = list_display


@admin.register(WalletTransfer)
class WalletTransferAdmin(admin.ModelAdmin):
    list_display = [
        "sender_account",
        "receiver_account_number",
        "amount",
        "time_sent",
    ]
    list_display_links = list_display
    search_fields = list_display


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "self_account",
        "amount",
        "created",
    ]
    list_display_links = list_display
    search_fields = list_display
