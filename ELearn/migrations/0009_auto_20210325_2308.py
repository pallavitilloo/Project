# Generated by Django 3.1.7 on 2021-03-26 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ELearn', '0008_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reciever',
            new_name='receiver',
        ),
    ]
