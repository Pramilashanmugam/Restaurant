from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Reservation, Table
from .forms import ReservationForm
# Create your views here.

# Index view for the homepage
class IndexView(TemplateView):
    template_name = 'reservations/index.html'

# List reservations for the logged-in user
class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

# Create a new reservation
class MakeReservationView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = 'make_reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update an existing reservation
class UpdateReservationView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'update_reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_list')

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

# Delete a reservation
class DeleteReservationView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('reservation_list')

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
