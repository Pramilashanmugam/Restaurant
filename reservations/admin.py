from django.contrib import admin
from .models import Reservation, Table


class ReservationAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Reservation model
    in the Django admin interface.

    Attributes:
        list_display (tuple): Specifies the fields to display in the list
        view of reservations.
        list_filter (tuple): Specifies the fields to filter by in the admin
        list view.
        search_fields (tuple): Specifies the fields to search by in the admin
        list view.
    """
    list_display = ('user', 'table', 'date', 'time', 'guests', 'phone')
    list_filter = ('date', 'time', 'user', 'table')
    search_fields = ('user__username', 'table__number', 'phone')


# Register your models here.
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Table)
