# Generated by Django 4.0 on 2023-12-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0036_vaccine_record_vaccination_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine_record',
            name='remarks',
            field=models.TextField(default=None),
        ),
    ]