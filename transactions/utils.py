import random
import requests

from . import models
import uuid


def generate_trx_refrence():
    while True:
        generated_trx_refrence = "".join([str(random.randint(0, 9)) for _ in range(15)])
        if not models.WalletTransfer.objects.filter(
            trx_reference=generated_trx_refrence
        ).exists():
            return generated_trx_refrence


def generate_transaction_reference():
    return str(uuid.uuid4().hex[:10])


def get_exchange_rate(target_currency, source_currency):
    url = f"https://api.exchangerate.host/convert?from={source_currency}&to={target_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate = float(data.get("result"))

    # # Store the conversion rate in the CurrencyConverter model
    # currency_converter, created = CurrencyConverter.objects.get_or_create(
    #     source_currency=source_currency,
    #     target_currency=target_currency,
    # )
    # currency_converter.conversion_rate = conversion_rate
    # currency_converter.save()

    return conversion_rate
