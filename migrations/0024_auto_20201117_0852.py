# Generated by Django 3.0.7 on 2020-11-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0023_auto_20201117_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
