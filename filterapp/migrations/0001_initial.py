# Generated by Django 3.2.7 on 2021-09-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=30)),
                ('joinning_date', models.DateField()),
            ],
        ),
    ]
