# Generated by Django 3.0.7 on 2020-07-02 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='arti',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('heading', models.CharField(max_length=200)),
                ('timeStamp', models.DateField(default=django.utils.timezone.now)),
                ('cUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
