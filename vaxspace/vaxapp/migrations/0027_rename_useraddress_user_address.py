# Generated by Django 4.0 on 2023-12-08 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vaxapp', '0026_useraddress_alter_barangay_healthworker_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAddress',
            new_name='user_address',
        ),
    ]
