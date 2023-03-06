# Generated by Django 4.1.5 on 2023-02-07 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RideRequestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('dateTime', models.DateTimeField()),
                ('num_passenger', models.PositiveBigIntegerField(default=1)),
                ('carType', models.CharField(choices=[('Any', 'Any'), ('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Crossover', 'Crossover'), ('Minivan', 'Minivan')], default='Any', max_length=20)),
                ('isShared', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('OPEN', 'OPEN'), ('COMFIRM', 'COMFIRM')], default='OPEN', max_length=20)),
                ('specialRequest', models.CharField(default='N/A', max_length=200, null=True)),
                ('driver', models.CharField(default=None, max_length=200, null=True)),
                ('spotAvaliableLeft', models.PositiveBigIntegerField(default=0)),
                ('driver_fname', models.CharField(default=None, max_length=200, null=True)),
                ('driver_lname', models.CharField(default=None, max_length=200, null=True)),
                ('license', models.CharField(default=None, max_length=200, null=True)),
                ('user', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sharer', models.ManyToManyField(related_name='sharer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SharerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('involvedRides', models.ManyToManyField(to='account.riderequestinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('carType', models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Crossover', 'Crossover'), ('Minivan', 'Minivan')], default='SUV', max_length=20)),
                ('max_passenger', models.PositiveBigIntegerField(default=1)),
                ('license', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]