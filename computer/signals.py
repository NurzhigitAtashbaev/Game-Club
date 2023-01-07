from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Computer


@receiver(post_save, sender=Computer)
def update_busy_status(sender, instance, **kwargs):
    if instance.busy_until is None or instance.busy_until == "00:00:00":
        # поле busy_until пустое
        instance.busy = False
        instance.save()
    if not instance.busy_until and instance.busy_until.blank:
        # поле busy_until пустое
        instance.busy = False
        instance.save()
