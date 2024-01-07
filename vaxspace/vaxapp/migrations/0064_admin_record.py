# Generated by Django 4.0 on 2024-01-02 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vaxapp', '0063_rename_vaccinator_vaccine_record_vaccinator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=100, null=True)),
                ('contact', models.IntegerField(null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('birth_height', models.IntegerField(null=True)),
                ('birth_weight', models.IntegerField(null=True)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaxapp.barangay')),
                ('child_record', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaxapp.vaccine_record')),
            ],
        ),
    ]
