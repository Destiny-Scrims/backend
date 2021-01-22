# Generated by Django 3.0.5 on 2021-01-21 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210121_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='numTeams',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='expiry_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]