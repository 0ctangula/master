# Generated by Django 3.0.4 on 2020-03-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blogconf_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogconf',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
