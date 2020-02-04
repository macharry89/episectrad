# Generated by Django 2.1 on 2019-03-08 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('id_letter', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
                ('value_indicator', models.IntegerField()),
                ('possible_combine', models.IntegerField()),
            ],
            options={
                'db_table': 'indicators',
            },
        ),
        migrations.CreateModel(
            name='IndicatorInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'indicator_input',
            },
        ),
        migrations.AddField(
            model_name='indicator',
            name='indicatorinputs',
            field=models.ManyToManyField(to='dashboard.IndicatorInput'),
        ),
    ]
