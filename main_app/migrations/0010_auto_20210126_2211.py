# Generated by Django 3.0.5 on 2021-01-27 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210126_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='id',
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
