# Generated by Django 5.2.3 on 2025-06-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_subject_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
