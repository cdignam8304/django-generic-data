# Generated by Django 2.2.12 on 2020-05-21 08:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200519_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 5, 21, 8, 7, 39, 573426, tzinfo=utc), verbose_name='Date of Birth'),
        ),
    ]
