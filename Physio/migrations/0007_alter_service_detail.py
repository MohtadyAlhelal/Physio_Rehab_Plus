# Generated by Django 5.0.6 on 2024-05-19 12:02

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Physio', '0006_alter_service_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='detail',
            field=tinymce.models.HTMLField(),
        ),
    ]