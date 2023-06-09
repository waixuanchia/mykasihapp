# Generated by Django 4.1.5 on 2023-04-19 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("officers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="officer",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
