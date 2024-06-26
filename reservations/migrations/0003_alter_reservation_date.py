# Generated by Django 5.0.6 on 2024-07-01 16:42

import django.utils.timezone
import reservations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_alter_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[reservations.models.validate_reservation_date]),
        ),
    ]
