from django.contrib import admin
from .models import Reservation, Table


# This class is to customize how the Reservation model to be displayed in the Django admin
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'guests', 'phone')
    list_filter = ('date', 'time', 'user', 'table')
    search_fields = ('user__username', 'table__number', 'phone')

# Register your models here.
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Table)
