# Generated by Django 2.1.11 on 2020-06-17 06:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200616_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 6, 12, 33, 618361, tzinfo=utc)),
        ),
    ]
