# Generated by Django 3.2.2 on 2021-07-08 19:15

from django.db import migrations
import django_db_constraints.operations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210708_2114'),
    ]

    operations = [
        django_db_constraints.operations.AlterConstraints(
            name='trip',
            db_constraints={'sourceIsNotDest': 'check (source != destination)'},
        ),
    ]
