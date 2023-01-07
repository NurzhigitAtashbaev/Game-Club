from django.db import transaction
from .models import Computer


def create_computers(n):
    computers = []
    for i in range(n):
        computers.append(Computer(number=i, busy=False, time_busy=None, price=0))
    Computer.objects.bulk_create(computers)


# Create 1000 computers
create_computers(1000)
