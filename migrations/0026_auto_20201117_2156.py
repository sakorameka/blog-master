# Generated by Django 3.0.7 on 2020-11-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0025_auto_20201117_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]