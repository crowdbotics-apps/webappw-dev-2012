# Generated by Django 2.2.11 on 2020-03-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_customtext_temp"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="temp2",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
