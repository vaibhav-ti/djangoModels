# Generated by Django 4.0.8 on 2022-12-20 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectaccess',
            name='created_by',
        ),
    ]
