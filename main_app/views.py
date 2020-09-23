from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Unit, Ticket, Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .forms import TicketForm

# Create your views here.
@login_required
def home(request):
    return redirect('index')

@login_required
def tickets_index(request):
    try:
        profile = request.user.profile
        unit = profile.unit
        tickets = unit.ticket_set.all()
        # ticket_form = TicketForm()
        return render(request, 'tickets/index.html', {'profile': profile, 'tickets': tickets, 'unit': unit})
    except Profile.DoesNotExist:
        profile = 0
        tickets = Ticket.objects.filter(unit=profile)
        return render(request, 'tickets/index.html', {'profile': profile, 'tickets': tickets})
        
@login_required
def tickets_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'tickets/detail.html', {'ticket': ticket})

@login_required
def tickets_create(request, unit_id):
    unit = Unit.objects.get(id=unit_id)
    ticket_form = TicketForm()
    form = TicketForm(request.POST)
    if form.is_valid():
        new_ticket = form.save(commit=False)
        new_ticket.unit_id = unit_id
        new_ticket.save()
        return redirect('index')
    return render(request, 'tickets/ticket_form.html', {'unit': unit, 'ticket_form': ticket_form})

class TicketDelete(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = '/tickets/'

class TicketUpdate(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['category', 'priority', 'location', 'description']

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class NewLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        return context

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['phone']
    success_url = '/tickets/'
