# Generated by Django 4.0 on 2023-12-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0047_schedule_date_of_birth_vaccine_record_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date_of_birth',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vaccine_record',
            name='date_of_birth',
            field=models.TextField(null=True),
        ),
    ]
