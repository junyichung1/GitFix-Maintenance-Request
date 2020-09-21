from django.contrib import admin
from .models import Ticket, Unit, Profile

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Unit)
admin.site.register(Profile)