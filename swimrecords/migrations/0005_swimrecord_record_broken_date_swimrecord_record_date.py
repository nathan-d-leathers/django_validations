# Generated by Django 4.0.6 on 2022-07-08 03:13

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimrecords', '0004_swimrecord_distance_swimrecord_stroke_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimrecord',
            name='record_broken_date',
            field=models.DateTimeField(default=None, validators=[django.core.validators.MaxValueValidator(limit_value=models.DateTimeField(default=None, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]))]),
        ),
        migrations.AddField(
            model_name='swimrecord',
            name='record_date',
            field=models.DateTimeField(default=None, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date.today)]),
        ),
    ]