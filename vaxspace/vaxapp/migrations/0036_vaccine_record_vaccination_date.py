# Generated by Django 4.0 on 2023-12-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0035_alter_schedule_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine_record',
            name='vaccination_date',
            field=models.DateField(default=None),
        ),
    ]
