# Generated by Django 5.1.3 on 2024-12-04 07:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DentalcareApp', '0003_appointment_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
