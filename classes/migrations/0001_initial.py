# Generated by Django 4.2.1 on 2023-05-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EnglishClass",
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
                ("date", models.DateField()),
                ("time_start", models.TimeField()),
                ("time_end", models.TimeField()),
                ("eventId", models.CharField(max_length=256)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ToBeDone", "To be Done"),
                            ("InProgress", "In Progress"),
                            ("Done", "Done"),
                        ],
                        default="ToBeDone",
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
