# Generated by Django 2.2.11 on 2020-03-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_customtext_temp3'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='csc',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
