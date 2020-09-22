from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime

# type:'timestamp with time zone'

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
class Unit(models.Model):
    unit_number = models.CharField(max_length=10)
    unit_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.unit_number
    
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
    status =models.CharField(
        max_length=3,
        choices=STATUSES,
        default='NEW',
    )
    date_created = models.DateTimeField(default=datetime.now)
    completion_date = models.TimeField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username