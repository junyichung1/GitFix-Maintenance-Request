from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'priority', 'location', 'description']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
