# Generated by Django 2.2.4 on 2019-11-29 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191125_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_comments', to='blog.BlogPost'),
        ),
    ]