from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Reservation, Table
from .forms import ReservationForm
# Create your views here.

class Index(TemplateView):
    template_name = 'reservations/index.html'

class ReservationListView(generic.ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservation_list'