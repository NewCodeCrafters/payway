from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from account.models import Account
from .models import Profiles


@receiver(post_save, sender=Profiles)
def create_account_signals(sender, instance, created, **kwargs):
    if created and instance.currency:
        Account.objects.create(
            user=instance.user,
            currency=instance.currency,
            balance=0,
            is_approved=False,
        )
