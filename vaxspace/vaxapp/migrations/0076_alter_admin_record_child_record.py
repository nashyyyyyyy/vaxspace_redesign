# Generated by Django 4.0 on 2024-01-03 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0075_alter_admin_record_child_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_record',
            name='child_record',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='vaxapp.vaccine_record'),
        ),
    ]
