from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tickets/', views.tickets_index, name='index'),
    path('logout/', views.NewLogoutView.as_view()),
    # path('tickets/<int:ticket_id>/', views.tickets_detail, name='detail'),
    path('units/<int:unit_id>/create_ticket/', views.tickets_create, name='tickets_create'),
]