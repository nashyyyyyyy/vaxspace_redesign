# Generated by Django 4.0 on 2023-12-19 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0032_rename_brgy_schedule_brgyid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='brgyId',
            new_name='brgy',
        ),
    ]