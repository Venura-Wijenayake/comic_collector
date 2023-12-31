# Generated by Django 4.2.3 on 2023-08-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("description", models.TextField(max_length=250)),
                ("writer", models.CharField(max_length=100)),
                ("penciler", models.CharField(max_length=100)),
            ],
        ),
    ]
