# Generated by Django 4.0 on 2023-12-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0017_schedule_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='vaccine_info',
            field=models.TextField(default=None),
        ),
    ]