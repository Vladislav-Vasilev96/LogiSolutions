# Generated by Django 4.2.3 on 2023-08-06 09:26

import LogiSolutions.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_warehouse_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='contact_person',
            field=models.CharField(default='+359', max_length=13, validators=[LogiSolutions.core.validators.validate_phone_number]),
        ),
    ]