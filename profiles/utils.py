import random
import requests
import string

from . import models


# def get_exchange_rate(target_currency, source_currency):
#     url = f"https://api.exchangerate.host/convert?from={source_currency}&to={target_currency}"
#     response = requests.get(url)
#     data = response.json()
#     conversion_rate = float(data.get("result"))

#     # # Store the conversion rate in the CurrencyConverter model
#     # currency_converter, created = CurrencyConverter.objects.get_or_create(
#     #     source_currency=source_currency,
#     #     target_currency=target_currency,
#     # )
#     # currency_converter.conversion_rate = conversion_rate
#     # currency_converter.save()

#     return conversion_rate


def generate_unique_account_number():
    while True:
        account_number = "2"
        account_number += "".join(random.choices(string.digits, k=9))
        if not models.Profiles.objects.filter(account_number=account_number).exists():
            return account_number
