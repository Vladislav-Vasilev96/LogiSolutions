# Generated by Django 4.2.3 on 2023-08-11 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_alter_warehouse_contact_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
