# Generated by Django 5.0.6 on 2024-05-19 11:19

import django_editorjs.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Physio', '0005_alter_service_detail_alter_service_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='detail',
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]
