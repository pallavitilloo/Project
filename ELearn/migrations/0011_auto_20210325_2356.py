# Generated by Django 3.1.7 on 2021-03-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ELearn', '0010_message_receivers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receivers',
            field=models.CharField(max_length=255, verbose_name='To'),
        ),
    ]
