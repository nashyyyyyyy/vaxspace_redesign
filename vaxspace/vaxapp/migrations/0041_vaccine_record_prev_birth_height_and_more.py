# Generated by Django 4.0 on 2023-12-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0040_alter_vaccine_record_vaccination_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine_record',
            name='prev_birth_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vaccine_record',
            name='prev_birth_weight',
            field=models.IntegerField(null=True),
        ),
    ]