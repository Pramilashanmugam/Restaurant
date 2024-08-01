from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Reservation, Table
from django.utils import timezone
from datetime import timedelta


def validate_phone(value):
    """
    Validates that the phone number contains only digits.
    Args:
        value (str): The phone number to validate.
    Raises:
        ValidationError: If the phone number contains non-digit characters.
    """
    if not value.isdigit():
        raise ValidationError(
            'Phone numbers can only be numbers. Please check your entry.'
        )


def validate_guests(value):
    """
    Validates that the number of guests is greater than zero.
    Args:
        value (int): The number of guests to validate.
    Raises:
        ValidationError: If the number of guests is zero or negative.
    """
    if value <= 0:
        raise ValidationError(
            'The number of guests must be greater than zero. '
            'Please enter a valid number.'
        )


def validate_name(value):
    """
    Validates that the name contains only alphabetic characters.
    Args:
        value (str): The name to validate.
    Raises:
        ValidationError: If the name contains non-alphabetic characters.
    """
    if not value.isalpha():
        raise ValidationError(
            'Name can only contain alphabetic characters. '
            'Please check your entry.'
        )


class ReservationForm(forms.ModelForm):
    """
    Form for creating and updating reservations.
    Fields:
        table (ForeignKey): The table for the reservation.
        name (CharField): The name of the person making the reservation.
        date (DateField): Only from current date is accepted.
        time (CharField): Can choose only from the given time slots.
        guests (IntegerField): The number of guests.
        phone (CharField): The phone number of the user making the reservation.
        notes (TextField): Additional notes for the reservation.
    """

    phone = forms.CharField(max_length=20, validators=[validate_phone],
                            widget=forms.TextInput(
                                attrs={'class': 'form-control'}))
    guests = forms.IntegerField(validators=[validate_guests],
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=100, validators=[validate_name],
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}))
    notes = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'maxlength': 1000}
        )
    )

    class Meta:
        model = Reservation
        fields = ['table', 'name', 'date', 'time', 'guests', 'phone', 'notes']
        widgets = {
            'table': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.Select(choices=[
                ('12:00', '12:00 PM'), ('12:15', '12:15 PM'),
                ('12:30', '12:30 PM'), ('12:45', '12:45 PM'),
                ('13:00', '1:00 PM'), ('13:15', '1:15 PM'),
                ('13:30', '1:30 PM'), ('13:45', '1:45 PM'),
                ('14:00', '2:00 PM'), ('14:15', '2:15 PM'),
                ('14:30', '2:30 PM'), ('17:30', '5:30 PM'),
                ('17:45', '5:45 PM'), ('18:00', '6:00 PM'),
                ('18:15', '6:15 PM'), ('18:30', '6:30 PM'),
                ('18:45', '6:45 PM'), ('19:00', '7:00 PM'),
                ('19:15', '7:15 PM'), ('19:30', '7:30 PM'),
                ('19:45', '7:45 PM'), ('20:00', '8:00 PM'),
                ('20:15', '8:15 PM'), ('20:30', '8:30 PM'),
                ('20:45', '8:45 PM'), ('21:00', '9:00 PM'),
                ('21:15', '9:15 PM'), ('21:30', '9:30 PM'),
                ('21:45', '9:45 PM'), ('22:00', '10:00 PM')
            ], attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'min': (timezone.now() + timedelta(days=1)).date().isoformat(),
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_date(self):
        """
        Custom validation for the date field.
        Ensures the reservation date is at least one day after the current date
        and not on a Monday.
        Raises:
            ValidationError: If the reservation date is within one day of
            the current date or on a Monday.
        """
        date = self.cleaned_data.get('date')
        if date:
            if date.weekday() == 0:  # Monday is 0
                raise ValidationError('Sorry we are closed on Mondays. '
                                      'Please choose another day.')
            if date <= timezone.now().date() + timedelta(days=0):
                raise ValidationError('Online reservations can only be made'
                                      ' at least one day in advance. '
                                      'Please choose another date.')
        return date

    def clean(self):
        """
        Custom validation for the form.
        Ensures that the number of guests does not exceed the table's capacity.
        Returns:
            dict: The cleaned data.
        Raises:
            ValidationError: If the number of guests exceeds the table's
            capacity.
        """
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        guests = cleaned_data.get('guests')

        if table and guests:
            if guests > table.capacity:
                self.add_error('guests', f"The number of guests exceeds the "
                               "table's capacity. "
                               "Please choose another table.")

        return cleaned_data
