from django.urls import path
from .views import * # imports all the functions from views

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservations/reserve/', MakeReservationView.as_view(), name='make_reservation'),
    path('reservations/<int:pk>/update/', UpdateReservationView.as_view(), name='update_reservation'),
    path('reservations/<int:pk>/delete/', DeleteReservationView.as_view(), name='delete_reservation'),
]