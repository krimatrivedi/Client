# Generated by Django 3.0.9 on 2022-11-18 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0020_auto_20221118_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examples.Book'),
        ),
    ]
