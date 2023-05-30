from asyncio import sleep
from threading import Thread

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from lm.models import Subject
from lm.telegram import send_telegram_message


class Notification(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    message = models.TextField()

    def __str__(self):
        return self.message


@receiver(post_save, sender=Notification)
def on_notification_save_in_thread(sender, instance: Notification, created, **kwargs):
    if created:
        thread = Thread(target=on_notification_save, args=(instance,))
        thread.start()


def on_notification_save(instance):
    sleep(1)

    text = f"""
    NOTIFICATION for {instance.subject }:
    {instance.message}
    """

    send_telegram_message(text)
