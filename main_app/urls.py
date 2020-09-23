from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tickets/', views.tickets_index, name='index'),
    path('logout/', views.NewLogoutView.as_view()),
    path('tickets/<int:ticket_id>/detail/', views.tickets_detail, name='detail'),
    path('units/<int:unit_id>/create_ticket/', views.tickets_create, name='tickets_create'),
    path('tickets/<int:pk>/delete/', views.TicketDelete.as_view(), name='tickets_delete'),
    path('tickets/<int:pk>/update/', views.TicketUpdate.as_view(), name='tickets_update'),
    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    # path('password/<int:pk>/update/', views.Update.as_view(), name='user_update'),
    path('user/password_change/', views.change_password, name='change_password'),
]