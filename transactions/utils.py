import random
import requests
from django.conf import settings
from . import models
import uuid
from decimal import Decimal


def generate_trx_refrence():
    while True:
        generated_trx_refrence = "".join([str(random.randint(0, 9)) for _ in range(15)])
        if not models.WalletTransfer.objects.filter(
            trx_reference=generated_trx_refrence
        ).exists():
            return generated_trx_refrence


def generate_trf_id():
    while True:
        generate_trf_id = "".join([str(random.randint(0, 9)) for _ in range(15)])
        if not models.Transactions.objects.filter(trf_id=generate_trf_id).exists():
            return generate_trf_id


def generate_transaction_reference():
    return str(uuid.uuid4().hex[:10])


def get_exchange_rate(target_currency, source_currency):
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {
        "from": f"{source_currency}",
        "to": f"{target_currency}",
        "amount": "1",
    }

    headers = {
        "X-RapidAPI-Key": f"{settings.CURRENCY_API}",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    values = response.json()
    rate = values["result"].get("convertedAmount")

    return Decimal(rate)
