# Generated by Django 3.0.9 on 2022-11-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0005_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, unique=True),
        ),
    ]
