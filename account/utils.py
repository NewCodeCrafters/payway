import random
from . import models


def generate_naira_account_number(currency):
    while True:
        prefix = "21"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_canada_account_number(currency):
    while True:
        prefix = "22"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_ghc_account_number(currency):
    while True:
        prefix = "23"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_aud_account_number(currency):
    while True:
        prefix = "24"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_pounds_account_number(currency):
    while True:
        prefix = "25"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_euros_account_number(currency):
    while True:
        prefix = "26"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number


def generate_account_number(currency):
    while True:
        prefix = "10"
        gen_account_number = "".join([str(random.randint(0, 9)) for _ in range(9)])
        new_account_number = prefix + gen_account_number
        if not models.Account.objects.filter(
            account_number=new_account_number, currency=currency
        ).exists():
            return new_account_number
