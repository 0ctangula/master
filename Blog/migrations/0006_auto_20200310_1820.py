# Generated by Django 3.0.4 on 2020-03-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blog_blogtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogtitle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
