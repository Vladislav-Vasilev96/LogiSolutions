# Generated by Django 4.2.3 on 2023-08-11 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0007_alter_cargo_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
