# Generated by Django 4.0.8 on 2022-12-20 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicetemplate',
            old_name='author_id',
            new_name='author',
        ),
    ]
