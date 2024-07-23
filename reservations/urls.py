from django.urls import path
from . import views

"""
URL patterns for the restaurant booking application.

This list includes URL routes and their corresponding view functions
or classes.

1. Home Page
2. Menu Page
3. Reservation List
4. Make a Reservation
5. Update a Reservation
    Allows the user to update an existing reservation.
    The primary key (pk) of the reservation is required.
6. Delete a Reservation
    Allows the user to delete an existing reservation.
    The primary key (pk) of the reservation is required.
"""
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/make/', views.make_reservation,
         name='make_reservation'),
    path('reservations/update/<int:pk>/', views.update_reservation,
         name='update_reservation'),
    path('reservations/delete/<int:pk>/', views.delete_reservation,
         name='delete_reservation'),
]
