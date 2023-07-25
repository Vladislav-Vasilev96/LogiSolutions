# Generated by Django 4.2.3 on 2023-07-23 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_profile_profile_user_alter_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Truck Owner', 'TRUCK_OWNER'), ('Cargo Owner', 'CARGO_OWNER')], default='Truck Owner', max_length=11),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]