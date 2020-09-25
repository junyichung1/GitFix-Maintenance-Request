#  IMPORT AND INCLUDES FOR VIEWS.PY

import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Unit, Ticket, Profile, Photo
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .forms import TicketForm, UserForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# AWS INFORMATION

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'gitfix'


# HOME

@login_required
def home(request):
    return redirect('index')


# USER DASHBOARD


@login_required
def tickets_index(request):
    try:
        profile = request.user.profile
        unit = profile.unit
        tickets = unit.ticket_set.all().order_by('-date_created')[0:10]
        return render(request, 'tickets/index.html', {'profile': profile, 'tickets': tickets, 'unit': unit})
    except Profile.DoesNotExist:
        return render(request, 'registration/done.html')


# TICKET DETAILS


@login_required
def tickets_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'tickets/detail.html', {'ticket': ticket})


# ADD NEW TICKET


@login_required
def tickets_create(request, unit_id):
    unit = Unit.objects.get(id=unit_id)
    ticket_form = TicketForm()
    form = TicketForm(request.POST)
    if form.is_valid():
        new_ticket = form.save(commit=False)
        new_ticket.unit_id = unit_id
        new_ticket.save()
        messages.success(request, 'Ticket created successfully. We\'ll get in touch with you soon')
        return redirect('index')
    return render(request, 'tickets/ticket_form.html', {'unit': unit, 'ticket_form': ticket_form})


# DELETE A TICKET


class TicketDelete(LoginRequiredMixin, SuccessMessageMixin,  DeleteView):
    model = Ticket
    success_url = '/tickets/'
    success_message = "Ticket was deleted successfully"


# UPDATE A TICKET


class TicketUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Ticket
    fields = ['category', 'priority', 'location', 'description']
    success_message = "Ticket was updated successfully"

# NEW USER - SIGNUP

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'registration/done.html')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# LOGOUT


class NewLogoutView(LogoutView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        success_message = "Logged out successfully"
        return context
    
# PHONE NUMBER UPDATE

class PhoneUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['phone']
    success_message = "Phone number was updated successfully"
    success_url = '/'
    def get_object(self):
        return self.request.user.profile


# CHANGE PASSWORD



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please read instructions below and try again.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', { 'form': form })
  
# EDIT USER INFO


@login_required
def edit_names(request, user_id):
    if request.method == "POST":
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User Information was successfully updated!')
            return redirect('index')
    else:
        form = UserForm(instance=request.user)
        return render(request, 'registration/edit_names.html')



@login_required
def add_photo(request, ticket_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, ticket_id=ticket_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', ticket_id=ticket_id)

# DELETE PHOTO

@login_required
def unassoc_photo(request, ticket_id, photo_id):
  photo = Photo.objects.get(id=photo_id)
  photo.delete()
  return redirect('detail', ticket_id=ticket_id)

# INFO PAGES

def about(request):
    return render(request, 'about.html')

def how(request):
    return render(request, 'how.html')

def contact(request):
    return render(request, 'contact.html')
