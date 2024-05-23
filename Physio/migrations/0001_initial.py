# Generated by Django 5.0.6 on 2024-05-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_cover', models.ImageField(upload_to='events/')),
                ('date', models.DateField()),
                ('details', models.TextField()),
                ('event_images', models.ImageField(upload_to='events/')),
            ],
        ),
    ]