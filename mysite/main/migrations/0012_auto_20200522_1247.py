# Generated by Django 2.2.12 on 2020-05-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200522_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_active',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=8),
        ),
    ]