# Generated by Django 2.2.7 on 2019-11-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0004_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_images', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'verbose_name': 'Contact'},
        ),
    ]
