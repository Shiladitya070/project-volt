# Generated by Django 2.1.11 on 2020-06-14 05:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200614_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 5, 30, 11, 433645, tzinfo=utc)),
        ),
    ]
