from django.db import models
from django.contrib.auth.models import User

CATEGORIES = (
    ('ELE', 'Electric'),
    ('PLU', 'Plumbing'),
    ('LIG', 'Light fixtures'),
)

PRIORITIES = (
    ('L', 'LOW'),
    ('M', 'MEDIUM'),
    ('H', 'HIGH'),
)

STATUSES = (
    ('NEW', 'New Ticket'),
    ('PEN', 'Pending'),
    ('COM', 'Completed'),
)


# Create your models here.
class Ticket(models.Model):
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES,
    )
    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
    )
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    unit_id = models.IntegerField()
    status =models.CharField(
        max_length=3,
        choices=STATUSES,
    )
    date_created = models.TimeField()
    completion_date = models.TimeField()

class Unit(models.Model):
    unit_number = models.CharField(max_length=10)
    unit_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

