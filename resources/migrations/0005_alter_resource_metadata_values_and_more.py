# Generated by Django 4.0.8 on 2022-12-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_rename_enviornment_resource_environment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='metadata_values',
            field=models.JSONField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='user_input',
            field=models.JSONField(max_length=128, null=True),
        ),
    ]
