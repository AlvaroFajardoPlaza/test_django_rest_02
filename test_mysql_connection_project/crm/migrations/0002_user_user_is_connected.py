# Generated by Django 5.0.1 on 2024-01-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_is_connected",
            field=models.BooleanField(default=False),
        ),
    ]
