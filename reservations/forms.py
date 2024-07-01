from django import forms
from django.contrib import admin
from .models import Reservation, Table

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget = forms.Select(choices=[
            ('12:00', '12:00 PM'), ('12:15', '12:15 PM'), ('12:30', '12:30 PM'), ('12:45', '12:45 PM'),
            ('13:00', '1:00 PM'), ('13:15', '1:15 PM'), ('13:30', '1:30 PM'), ('13:45', '1:45 PM'),
            ('14:00', '2:00 PM'), ('14:15', '2:15 PM'), ('14:30', '2:30 PM'),
            ('17:30', '5:30 PM'), ('17:45', '5:45 PM'), ('18:00', '6:00 PM'), ('18:15', '6:15 PM'),
            ('18:30', '6:30 PM'), ('18:45', '6:45 PM'), ('19:00', '7:00 PM'), ('19:15', '7:15 PM'),
            ('19:30', '7:30 PM'), ('19:45', '7:45 PM'), ('20:00', '8:00 PM'), ('20:15', '8:15 PM'),
            ('20:30', '8:30 PM'), ('20:45', '8:45 PM'), ('21:00', '9:00 PM'), ('21:15', '9:15 PM'),
            ('21:30', '9:30 PM'), ('21:45', '9:45 PM'), ('22:00', '10:00 PM')
        ])

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Table)