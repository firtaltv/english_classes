# Generated by Django 4.2.1 on 2023-05-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_date_registration_remove_user_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]