# Generated by Django 2.2.7 on 2019-11-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='bmr_value',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
