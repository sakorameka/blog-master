# Generated by Django 3.0.7 on 2020-10-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='blogapp.Comment'),
        ),
    ]
