# Generated by Django 3.0.5 on 2021-01-26 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210125_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
