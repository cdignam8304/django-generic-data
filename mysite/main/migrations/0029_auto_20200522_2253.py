# Generated by Django 2.2.12 on 2020-05-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20200522_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='generic',
            name='amount1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='amount1'),
        ),
        migrations.AddField(
            model_name='generic',
            name='amount2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='amount2'),
        ),
        migrations.AddField(
            model_name='schema',
            name='amount1',
            field=models.CharField(blank=True, max_length=200, verbose_name='date3'),
        ),
        migrations.AddField(
            model_name='schema',
            name='amount2',
            field=models.CharField(blank=True, max_length=200, verbose_name='date3'),
        ),
    ]