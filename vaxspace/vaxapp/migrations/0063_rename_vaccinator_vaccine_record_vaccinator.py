# Generated by Django 4.0 on 2024-01-02 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0062_alter_vaccine_record_vaccinator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccine_record',
            old_name='Vaccinator',
            new_name='vaccinator',
        ),
    ]
