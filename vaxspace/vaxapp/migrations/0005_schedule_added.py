# Generated by Django 4.0 on 2023-12-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vaxapp', '0004_remove_schedule_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='added',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]