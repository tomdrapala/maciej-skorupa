# Generated by Django 3.0.3 on 2021-01-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20201015_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
