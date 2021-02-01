# Generated by Django 3.0.3 on 2020-10-13 09:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201009_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 9, 49, 29, 703413, tzinfo=utc)),
        ),
    ]