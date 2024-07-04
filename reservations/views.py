from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Reservation, Table
from .forms import ReservationForm

# Index view for the homepage
class Index(TemplateView):
    template_name = 'reservations/index.html'

class Menu(TemplateView):
    template_name = 'reservations/menu.html'

# View to list reservations for the logged-in user
@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

# View to make a new reservation
@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})

# View to update an existing reservation
@login_required
def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/make_reservation.html', {'form': form})

# View to delete a reservation
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/confirm_delete.html', {'reservation': reservation})