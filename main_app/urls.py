from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tickets/', views.tickets_index, name='index'),
    path('logout/', views.NewLogoutView.as_view()),
    path('tickets/create/', views.TicketCreate.as_view(), name='tickets_create'),
]