from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Table {self.number} (Capacity: {self.capacity})'

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return f'Reservation for {self.user.username} on {self.date} at {self.time}'