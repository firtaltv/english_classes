# Generated by Django 4.2.1 on 2023-05-24 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("classes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="englishclass",
            name="students",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="englishclass",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teacher",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
