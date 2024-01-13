# Generated by Django 5.0.1 on 2024-01-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestModel01",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="assets/images")),
                ("url", models.URLField(blank=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de creación"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Última modificación"
                    ),
                ),
            ],
        ),
    ]