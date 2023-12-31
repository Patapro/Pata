# Generated by Django 4.2.5 on 2023-09-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProviderPersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firtName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNumber', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProviderWorkInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('yearsOfExperince', models.IntegerField(max_length=10)),
            ],
        ),
    ]
