# Generated by Django 4.0 on 2024-01-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0059_vaccine_record_vaccinator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine_record',
            name='Vaccinator',
            field=models.TextField(default=None),
        ),
    ]