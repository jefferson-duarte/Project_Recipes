# Generated by Django 5.0.4 on 2024-06-17 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='object_id',
        ),
    ]
