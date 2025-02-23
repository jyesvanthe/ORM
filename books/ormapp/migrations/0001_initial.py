# Generated by Django 5.0.3 on 2024-03-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='railway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_code', models.CharField(help_text='railway train_code', max_length=20)),
                ('train_name', models.CharField(max_length=100)),
                ('start_time', models.IntegerField()),
                ('End_time', models.IntegerField()),
                ('start_station_code', models.IntegerField()),
                ('end_station_code', models.IntegerField()),
            ],
        ),
    ]
