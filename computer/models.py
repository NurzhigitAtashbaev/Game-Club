from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Computer(models.Model):
    category = models.CharField(max_length=100)
    number = models.IntegerField(null=False, blank=False)
    busy = models.BooleanField(default=False)
    busy_until = models.TimeField(default="00:00:00")
    price = models.IntegerField()

    def clean(self):
        if self.busy_until == "00:00:00" or (not self.busy_until and self.busy_until.blank):
            self.busy = False
        super().clean()

    @classmethod
    def update_busy_status(cls):
        for computer in cls.objects.all():
            if computer.busy_until == "00:00:00" or (not computer.busy_until and computer.busy_until.blank):
                computer.busy = False
                computer.save()


# def create_computers(n):
#     computers = []
#     for i in range(n):
#         computers.append(Computer(category='VIP', number=i,  price=200))
#     Computer.objects.bulk_create(computers)
#
#
# # Create 1000 computers
#
# create_computers(20)
@receiver(post_save, sender=Computer)
def update_busy_status(sender, instance, **kwargs):
    if sender.busy_until is None or sender.busy_until == "00:00:00":
        # поле busy_until пустое
        sender.instance.busy = False
        instance.save()
    if not instance.busy_until and instance.busy_until.blank:
        # поле busy_until пустое
        instance.busy = False
        instance.save()
