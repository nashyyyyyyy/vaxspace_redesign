# Generated by Django 4.0 on 2024-01-05 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0082_vaccine_record_brgy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_record',
            name='child_record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaxapp.vaccine_record'),
        ),
    ]
