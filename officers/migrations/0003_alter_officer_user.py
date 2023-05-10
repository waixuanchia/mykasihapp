# Generated by Django 4.1.5 on 2023-05-04 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("officers", "0002_alter_officer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="officer",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="officer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
