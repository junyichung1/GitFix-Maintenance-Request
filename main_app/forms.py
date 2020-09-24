from django.forms import ModelForm
from .models import Ticket, User, Profile

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'priority', 'location', 'description']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    
# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['phone']