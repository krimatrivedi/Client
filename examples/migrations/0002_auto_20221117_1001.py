# Generated by Django 3.0.9 on 2022-11-17 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='clientname',
        ),
    ]
