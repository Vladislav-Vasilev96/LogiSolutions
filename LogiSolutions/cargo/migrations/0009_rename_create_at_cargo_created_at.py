# Generated by Django 4.2.3 on 2023-08-11 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0008_cargo_create_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
