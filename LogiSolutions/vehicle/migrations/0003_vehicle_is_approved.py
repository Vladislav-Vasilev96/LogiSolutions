# Generated by Django 4.2.3 on 2023-07-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_remove_vehicle_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
