import random
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
