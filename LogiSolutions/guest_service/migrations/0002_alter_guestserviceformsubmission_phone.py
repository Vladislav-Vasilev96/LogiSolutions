# Generated by Django 4.2.3 on 2023-07-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestserviceformsubmission',
            name='phone',
            field=models.CharField(default='+359', max_length=13),
        ),
    ]
