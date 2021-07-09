# Generated by Django 3.2.4 on 2021-07-09 21:14

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
            name='Station',
            fields=[
                ('id', models.IntegerField(default=-1, primary_key=True, serialize=False)),
                ('stationName', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_seats', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TrainDest', to='blog.station')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TrainSource', to='blog.station')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_Time', models.TimeField()),
                ('end_Time', models.TimeField()),
                ('price', models.FloatField(default=0)),
                ('Remaining_seats', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TripDest', to='blog.station')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TripSource', to='blog.station')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TripTrain', to='blog.train')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField(default=-1)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookTrips', to='blog.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('trip', 'user', 'seats')},
            },
        ),
    ]
