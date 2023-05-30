from django.db.models.signals import post_save
from django.dispatch import receiver

from lm.models import Notification
from lm.tasks import on_order_save


@receiver(post_save, sender=Notification)
def on_order_save_in_thread(sender, instance: Notification, created, **kwargs):
    if created:
        on_order_save.delay(instance.id)
