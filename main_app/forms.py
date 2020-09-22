from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'priority', 'location', 'description']