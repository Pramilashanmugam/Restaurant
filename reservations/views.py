from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Reservation, Table
from .forms import ReservationForm


class Index(TemplateView):
    """
    View for rendering the homepage.

    Attributes:
        template_name (str): The path to the template used to render the view.
    """
    template_name = 'reservations/index.html'


class Menu(TemplateView):
    """
    View for rendering the menu page.

    Attributes:
        template_name (str): The path to the template used to render the view.
    """
    template_name = 'reservations/menu.html'


@login_required
def reservation_list(request):
    """
    View to list reservations for the logged-in user.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template displaying the list of
        reservations.
    """
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html',
                           {'reservations': reservations})


@login_required
def make_reservation(request):
    """
    View to make a new reservation.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template displaying the reservation form.
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html',
                  {'form': form})


@login_required
def update_reservation(request, pk):
    """
    View to update an existing reservation.

    Args:
        request: The HTTP request object.
        pk: The primary key of the reservation to update.

    Returns:
        HttpResponse: The rendered template displaying the reservation form.
    """
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/make_reservation.html',
                  {'form': form})


@login_required
def delete_reservation(request, pk):
    """
    View to delete a reservation.

    Args:
        request: The HTTP request object.
        pk: The primary key of the reservation to delete.

    Returns:
        HttpResponse: The rendered template confirming the deletion
        of the reservation.
    """
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/confirm_delete.html',
                  {'reservation': reservation})
