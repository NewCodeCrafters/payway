import random
from . import models


def generate_account_number(currency):
    while True:
        new_account_number = "".join([str(random.randint(0, 9)) for _ in range(11)])
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number
