from django.db import models

CATEGORIES = (
    ('ELE', 'Electric'),
    ('PLU', 'Plumbing'),
    ('LIG', 'Light fixtures'),
)

PRIORITIES = ('LOW', 'MEDIUM', 'HIGH')

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
        max_length=6,
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