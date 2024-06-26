# Generated by Django 5.0.6 on 2024-06-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('registration_date', models.DateField()),
                ('registartion_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('contact_person', models.CharField(max_length=100)),
                ('num_employees', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
