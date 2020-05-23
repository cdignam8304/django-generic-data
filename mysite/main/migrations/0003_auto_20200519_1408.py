# Generated by Django 2.2.12 on 2020-05-19 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200519_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 5, 19, 14, 8, 47, 768540), verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
