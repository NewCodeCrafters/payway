from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from profiles.models import Profiles

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_signals(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)
