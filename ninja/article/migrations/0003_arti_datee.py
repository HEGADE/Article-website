# Generated by Django 3.0.7 on 2020-07-04 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20200702_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='arti',
            name='datee',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
