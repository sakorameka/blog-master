# Generated by Django 3.0.7 on 2020-10-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20201022_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comment_text', models.TextField()),
                ('reply_comments', models.ManyToManyField(related_name='_comment_reply_comments_+', to='blogapp.Comment')),
            ],
        ),
    ]