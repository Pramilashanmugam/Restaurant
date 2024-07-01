from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Table {self.number} (Capacity: {self.capacity})'

# validating the booking time to match the restaurant open time
def validate_reservation_time(value):
    if not ((datetime.time(12, 0) <= value <= datetime.time(14, 30)) or (datetime.time(17, 30) <= value <= datetime.time(22, 0))):
        raise ValidationError("Reservation time must be between 12:00 to 14:30 or 17:30 to 22:00.")

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)  # This will set the date to the current date by default
    time = models.TimeField(validators=[validate_reservation_time])
    guests = models.IntegerField(default=0)
    phone = models.IntegerField()
    notes = models.TextField()

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.date} at {self.time}'