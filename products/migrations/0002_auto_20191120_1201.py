# Generated by Django 2.2.7 on 2019-11-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(default='Category', max_length=100),
        ),
    ]