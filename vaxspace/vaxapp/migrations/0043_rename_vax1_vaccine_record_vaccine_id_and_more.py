# Generated by Django 4.0 on 2023-12-29 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0042_rename_vaccine_id_vaccine_record_vax1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccine_record',
            old_name='vax1',
            new_name='vaccine_id',
        ),
        migrations.RenameField(
            model_name='vaccine_record',
            old_name='vax1_info',
            new_name='vaccine_info',
        ),
        migrations.RemoveField(
            model_name='vaccine_record',
            name='vax2',
        ),
        migrations.RemoveField(
            model_name='vaccine_record',
            name='vax2_info',
        ),
        migrations.RemoveField(
            model_name='vaccine_record',
            name='vax3',
        ),
        migrations.RemoveField(
            model_name='vaccine_record',
            name='vax3_info',
        ),
    ]
