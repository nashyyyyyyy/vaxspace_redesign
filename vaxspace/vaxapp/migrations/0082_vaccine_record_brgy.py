# Generated by Django 4.0 on 2024-01-05 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0081_rename_child_admin_record_child_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine_record',
            name='brgy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vaxapp.barangay'),
        ),
    ]