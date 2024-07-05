from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Table No: {self.number} can accomodate maximum {self.capacity} guest'

def validate_reservation_time(value):
    allowed_times = [
        datetime.time(hour=12, minute=0), datetime.time(hour=12, minute=15), datetime.time(hour=12, minute=30),
        datetime.time(hour=12, minute=45), datetime.time(hour=13, minute=0), datetime.time(hour=13, minute=15),
        datetime.time(hour=13, minute=30), datetime.time(hour=13, minute=45), datetime.time(hour=14, minute=0),
        datetime.time(hour=14, minute=15), datetime.time(hour=14, minute=30), datetime.time(hour=17, minute=30),
        datetime.time(hour=17, minute=45), datetime.time(hour=18, minute=0), datetime.time(hour=18, minute=15),
        datetime.time(hour=18, minute=30), datetime.time(hour=18, minute=45), datetime.time(hour=19, minute=0),
        datetime.time(hour=19, minute=15), datetime.time(hour=19, minute=30), datetime.time(hour=19, minute=45),
        datetime.time(hour=20, minute=0), datetime.time(hour=20, minute=15), datetime.time(hour=20, minute=30),
        datetime.time(hour=20, minute=45), datetime.time(hour=21, minute=0), datetime.time(hour=21, minute=15),
        datetime.time(hour=21, minute=30), datetime.time(hour=21, minute=45), datetime.time(hour=22, minute=0)
    ]
    if value not in allowed_times:
        raise ValidationError("Reservation time must be one of the allowed slots.")

def validate_reservation_date(value):
    today = timezone.now().date()
    six_months_from_today = today + datetime.timedelta(days=6*30)  # Approximation for 6 months
    if not (today <= value <= six_months_from_today):
        raise ValidationError("Reservation date must be between today and the next 6 months.")

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now, validators=[validate_reservation_date])
    time = models.TimeField(validators=[validate_reservation_time])
    guests = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    notes = models.TextField()

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f'Dear {self.name}, your booking for {self.guests} guests dated {self.date} at {self.time} is confirmed. Your {self.table}.'