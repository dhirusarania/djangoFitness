# Generated by Django 2.2.4 on 2019-12-27 05:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0010_bmrvalues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmrvalues',
            name='date_time',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]