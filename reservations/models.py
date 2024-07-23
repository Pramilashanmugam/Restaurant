from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Table(models.Model):
    """
    Model representing a table in the restaurant.

    Attributes:
        number(int): The unique number identifying the table.
        capacity(int): The max number of guests the table can accommodate.
    """
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the Table instance,
        showing the table number and its capacity.

        """
        return f'Table No: {self.number} can accommodate maximum {self.capacity} guests'


def validate_reservation_time(value):
    """
    Validate that the provided reservation time is within the allowed
    time slots.

    This function checks if the given time `value` is one of the predefined
    allowed reservation times. If the time is not allowed,
    it raises a ValidationError.

    Args:
        value (datetime.time): The reservation time to be validated.

    Raises:
        ValidationError: If the `value` is not in the list of allowed times.
    """
    allowed_times = [
        datetime.time(hour=12, minute=0), datetime.time(hour=12, minute=15),
        datetime.time(hour=12, minute=30), datetime.time(hour=12, minute=45),
        datetime.time(hour=13, minute=0), datetime.time(hour=13, minute=15),
        datetime.time(hour=13, minute=30), datetime.time(hour=13, minute=45),
        datetime.time(hour=14, minute=0), datetime.time(hour=14, minute=15),
        datetime.time(hour=14, minute=30), datetime.time(hour=17, minute=30),
        datetime.time(hour=17, minute=45), datetime.time(hour=18, minute=0),
        datetime.time(hour=18, minute=15), datetime.time(hour=18, minute=30),
        datetime.time(hour=18, minute=45), datetime.time(hour=19, minute=0),
        datetime.time(hour=19, minute=15), datetime.time(hour=19, minute=30),
        datetime.time(hour=19, minute=45), datetime.time(hour=20, minute=0),
        datetime.time(hour=20, minute=15), datetime.time(hour=20, minute=30),
        datetime.time(hour=20, minute=45), datetime.time(hour=21, minute=0),
        datetime.time(hour=21, minute=15), datetime.time(hour=21, minute=30),
        datetime.time(hour=21, minute=45), datetime.time(hour=22, minute=0)
    ]
    if value not in allowed_times:
        raise ValidationError(
         "Reservation time must be one of the allowed slots.")


def validate_reservation_date(value):
    """
    Validate that the provided reservation date is within the allowed range.

    This function checks if the given date `value` is between today and
    approximately six months from today. If the date is not within
    this range, it raises a ValidationError.
    """
    today = timezone.now().date()
    # Approximation for 6 months
    six_months_from_today = today + datetime.timedelta(days=6*30)
    if not (today <= value <= six_months_from_today):
        raise ValidationError(
            "Reservation date must be between today and the next 6 months.")


class Reservation(models.Model):
    """
    Model representing a reservation in the restaurant.

    Attributes:
        user (ForeignKey): Reference to the User who made the reservation.
        table (ForeignKey): Reference to the Table that is reserved.
        name (str): Name of the person who made the reservation.
        date (date): Date of the reservation.
        time (time): Time of the reservation.
        guests (int): Number of guests for the reservation.
        phone (str, but accepts only number validation given in forms.py):
        Contact phone number for the reservation.
        notes (str): Additional notes for the reservation.

    Meta:
        unique_together: Ensures that the combination of table,
        date, and time is unique.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now,
                            validators=[validate_reservation_date])
    time = models.TimeField(validators=[validate_reservation_time])
    guests = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    notes = models.TextField()

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        """
        Returns a string representation of the Reservation instance.

        The string includes the name, number of guests,
        date, time, and table information.
        """
        return (f'Dear {self.name}, your booking for {self.guests} guests on {self.date} at {self.time} is confirmed. Your table is {self.table}')
