# Generated by Django 4.0 on 2024-01-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0064_admin_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_record',
            name='added_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admin_record',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
