import random
from . import models


def generate_naira_account_number(currency):
    while True:
        new_account_number = "21".join([str(random.randint(0, 9)) for _ in range(9)])
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_account_number(currency):
    while True:
        new_account_number = "10".join([str(random.randint(0, 9)) for _ in range(11)])
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number
