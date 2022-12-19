# Generated by Django 4.0.2 on 2022-12-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_username', models.CharField(blank=True, max_length=128, null=True)),
                ('github_username', models.CharField(blank=True, max_length=128, null=True)),
                ('github_token', models.CharField(blank=True, max_length=128, null=True)),
                ('google_access_token', models.CharField(blank=True, max_length=2048, null=True)),
                ('google_refresh_token', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
