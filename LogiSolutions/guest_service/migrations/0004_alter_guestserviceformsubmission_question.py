# Generated by Django 4.2.3 on 2023-07-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_service', '0003_guestserviceformsubmission_date_asked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestserviceformsubmission',
            name='question',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]
